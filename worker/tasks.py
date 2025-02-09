from celery import shared_task
from app.instance.db_models import db, URLs
from sqids import Sqids
from sqlalchemy.exc import IntegrityError, OperationalError

@shared_task
def shorten_url(form_data, host_url):
    original_url = form_data['original_url']
    url = URLs(original_url=original_url)
    existing_entry = URLs.query.filter_by(original_url=original_url).first()
    if existing_entry:
        return existing_entry.shortened_url
    else:
        try:
            db.session.add(url)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f'Something went wrong {e}'
        try:
            sqids = Sqids(alphabet="FxnXM1kBN6cuhsAvjW3Co7l2RePyY8DwaU04Tzt9fHQrqSVKdpimLGIJOgb5ZE", min_length=8)
            unique_id = url.id
            short_id = sqids.encode([unique_id])
            short_url = f"{host_url}{short_id}"
            url.shortened_url = short_url
            db.session.commit()
            return short_url
        except IntegrityError:
            db.session.rollback()
        except OperationalError:
            db.session.rollback()
        except Exception:
            return 'Something went wrong, check logs for more details'

