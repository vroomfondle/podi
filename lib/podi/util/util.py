from ..rpc.library import list_episodes, list_tv_shows, list_movies

SORT_ASC=1
SORT_DESC=2

def retrieve_sorted_episodes(rpc, tv_show_id, sort_field='episodeid', sort_order=SORT_ASC, filters=None):
  """rpc should be a callable which will send the JSONRPC request to the Kodi server"""
  episodes =  rpc(list_episodes(tv_show_id, filters=filters)).get('episodes', [])
  for episode in sorted(
    episodes,
    key = lambda episode: episode[sort_field]):
    yield episode



def retrieve_sorted_movies(rpc, sort_field='movieid', sort_order=SORT_ASC, filters=None):
  """rpc should be a callable which will send the JSONRPC request to the Kodi server"""
  movies =  rpc(list_movies(filters=filters)).get('movies', [])
  for movie in sorted(
    movies,
    key = lambda movie: movie[sort_field]):
    yield movie



def retrieve_sorted_shows(rpc, tv_show_id = None, sort_field='tvshowid', sort_order=SORT_ASC, filters=None):
  """rpc should be a callable which will send the JSONRPC request to the Kodi server. tv_show_id can be used to restrict the list to a single id."""
  shows = rpc(list_tv_shows(filters=filters)).get('tvshows',[])
  for show in sorted(shows, key = lambda show: show[sort_field]):
    if (tv_show_id is None) or int(show['tvshowid']) == int(tv_show_id): 
      yield show



def list_to_dicts(key, input_list):
  """Turns a list of values into a list of single-entry dicts, with the provided key,
  so that the dicts can be used with pystache. The list is modified in-place."""
  for index in range(len(input_list)):
    input_list[index] = {key: input_list[index]}



def align_fields_for_display(items, fields):
  """
  Pads/truncates fields in each item to the specified length and puts the result in index ('display'+field_name).
  fields should be a list of tuples (str,int): (field_name, length).
  Returns the input list with padded items.
  """
  for item in items:
    for (field_name, length) in fields:
      if type(item[field_name]) is str or type(item[field_name]) is unicode:
        field_value = item[field_name]
      else:
        field_value = str(item[field_name])
      item['display{0}'.format(field_name)] = field_value[0:length-1].ljust(length)
  return items



def extract_video_runtime(video_item):
  """ 
  Finds the longest video stream in a given item, and returns a dict: 
    {'total_seconds':n, 'hours':n, 'minutes':n, 'seconds':n, 'str':"{hours}:{minutes}:{seconds}"}.
  video_item should be an item as returned in response to the JSON defined by the lib.podi.rpc.library methods, 
  and should include a sub-dict called 'streamdetails'.
  Raises a ValueError if there are no video streams (in the ValueError will be an attribute called 'default_runtime' which contains 0 hours/mins/secs; refer to this if you want to easily mimic the standard return format but with zero values).
  If the 'streamdetails' sub-dict is entirely missing, expect to see an IndexError.
  """
  if len(video_item['streamdetails']['video']) == 0:
    err = ValueError('No video streams found')
    err.default_runtime = {'total_seconds': 0, 'hours': 0, 'minutes': 0, 'seconds': 0, 'str':'00:00:00'}
    raise err
  total_seconds = int(max(video_item['streamdetails']['video'], 
    key = lambda item: int(item['duration']))['duration'])
  minutes, seconds = divmod(total_seconds, 60)
  hours, minutes = divmod(minutes, 60)
  return {
    'total_seconds': total_seconds,
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds,
    'str': "{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds),
  }
  
    
    
