import xbmcaddon
addon_id = xbmcaddon.Addon().getAddonInfo('id')

'''#####-----Build File-----#####'''
buildfile = 'https://duck-pirate.000webhostapp.com/builds.xml'

'''#####-----Notifications File-----#####'''
notify_url  = 'https://duck-pirate.000webhostapp.com/notify.txt'

'''#####-----Excludes-----#####'''
excludes  = [addon_id, 'packages', 'Addons33.db', 'kodi.log', 'script.module.certifi', 'script.module.chardet', 'script.module.idna', 'script.module.requests', 'script.module.urllib3', 'backups', 'plugin.video.whatever']