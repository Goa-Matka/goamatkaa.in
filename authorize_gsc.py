from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import json

SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def get_gsc_data():
    try:
        # Load service account credentials
        credentials = service_account.Credentials.from_service_account_file(
            'service-account.json',
            scopes=SCOPES
        )

        # Delegate domain-wide authority (if using Workspace)
        credentials = credentials.with_subject('admin@yourdomain.com')  # Optional

        # Build GSC service
        service = build('searchconsole', 'v1', credentials=credentials)

        # Query parameters (last 7 days)
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=7)
        
        request = {
            'startDate': start_date.strftime('%Y-%m-%d'),
            'endDate': end_date.strftime('%Y-%m-%d'),
            'dimensions': ['date', 'page', 'query'],  # Added more dimensions
            'rowLimit': 1000,
            'dataState': 'all'
        }

        # Execute query
        site_url = 'https://goamatkaa.in/'  # Replace with your property
        response = service.searchanalytics().query(
            siteUrl=site_url,
            body=request
        ).execute()

        # Process response
        if 'rows' not in response:
            return None

        # Format data for dashboard
        formatted_data = {
            'dates': [],
            'clicks': [],
            'impressions': [],
            'ctr': [],
            'position': [],
            'top_pages': [],
            'top_queries': []
        }

        # Aggregate data by date
        date_data = {}
        for row in response['rows']:
            date = row['keys'][0]
            if date not in date_data:
                date_data[date] = {
                    'clicks': 0,
                    'impressions': 0,
                    'ctr': 0,
                    'position': 0,
                    'count': 0
                }
            date_data[date]['clicks'] += row['clicks']
            date_data[date]['impressions'] += row['impressions']
            date_data[date]['ctr'] += row['ctr']
            date_data[date]['position'] += row['position']
            date_data[date]['count'] += 1

        # Calculate averages
        for date, metrics in date_data.items():
            formatted_data['dates'].append(date)
            formatted_data['clicks'].append(metrics['clicks'])
            formatted_data['impressions'].append(metrics['impressions'])
            formatted_data['ctr'].append(round((metrics['ctr'] / metrics['count']) * 100, 1))
            formatted_data['position'].append(round(metrics['position'] / metrics['count'], 1))

        # Extract top pages/queries (last 3 days)
        recent_data = [row for row in response['rows'] 
                      if row['keys'][0] >= (end_date - timedelta(days=3)).strftime('%Y-%m-%d')]
        
        # Top 5 pages by clicks
        top_pages = sorted(recent_data, key=lambda x: x['clicks'], reverse=True)[:5]
        formatted_data['top_pages'] = [
            {'url': row['keys'][1], 'clicks': row['clicks']} 
            for row in top_pages
        ]

        # Top 5 queries by impressions
        top_queries = sorted(recent_data, key=lambda x: x['impressions'], reverse=True)[:5]
        formatted_data['top_queries'] = [
            {'query': row['keys'][2], 'impressions': row['impressions']} 
            for row in top_queries
        ]

        return formatted_data

    except Exception as e:
        print(f"GSC API Error: {str(e)}")
        return None