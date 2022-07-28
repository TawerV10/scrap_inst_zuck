from instaloader import Instaloader, Profile
from fake_useragent import UserAgent
import os

L = Instaloader(sleep=True,
                quiet=False,
                user_agent=UserAgent().random,
                dirname_pattern=None,
                filename_pattern=None,
                download_pictures=True,
                download_videos=True,
                download_video_thumbnails=True,
                download_geotags=True,
                download_comments=True,
                save_metadata=True,
                compress_json=True,
                post_metadata_txt_pattern=None,
                storyitem_metadata_txt_pattern=None,
                max_connection_attempts=5,
                request_timeout=300.0,
                rate_controller=None,
                resume_prefix='iterator',
                check_resume_bbd=True,
                slide=None,
                fatal_status_codes=None,
                iphone_support=True,
                title_pattern=None,
                sanitize_paths=False)

L.login(os.getenv('USER'), os.getenv('PASSWORD'))

USERNAME = 'zuck'
profile = Profile.from_username(L.context, USERNAME)

for post in profile.get_posts():
    L.download_post(post, target=profile.username)