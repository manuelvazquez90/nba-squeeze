from datetime import datetime, timedelta, timezone

class Games:
    def run():
        model = {
            'errors': None,
            'data': None
        }
        now = datetime.now(timezone.utc).astimezone()
        results = [
            {
                'uuid': '4e81c06a-db0f-4281-b4cc-98208537772a' ,
                'display_name': 'Andrew Brown',
                'handle':  'andrewbrown',
                'message': 'Cloud is fun!',
                'created_at': now.isoformat()
            }
        ]

        model['data'] = results
        return model