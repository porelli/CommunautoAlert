import os
import apprise
from pkg_resources import resource_filename


class Notifications:
    def __init__(self, extra_config_notifications) -> None:
        asset = apprise.AppriseAsset()
        asset.app_id = 'CommunautoAlert'
        asset.app_desc = 'CommunautoAlert'
        asset.app_url = 'https://github.com/caronc/apprise'

        self.apobj = apprise.Apprise(asset=asset)

        config = apprise.AppriseConfig()
        # if a configuration file is provided...
        if extra_config_notifications != '':
            # ...check if it exists...
            if os.path.isfile(extra_config_notifications):
                # ..and add to apprise
                config.add(extra_config_notifications)
            else:
                # ...and return an error if file does not exist
                raise FileNotFoundError('The specified notifications file does not exist')
        else:
            # ...if it wasn't, add the default configuration
            config.add(resource_filename(__name__, 'resources/notifications.yaml'))

        self.apobj.add(config)
