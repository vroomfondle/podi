from ..rpc.library import list_episodes, list_tv_shows

def retrieve_sorted_episodes(rpc, tv_show_id, sort_field='episodeid', filters=None):
  """rpc should be a callable which will send the JSONRPC request to the Kodi server"""
  episodes =  rpc(list_episodes(tv_show_id)).get('episodes', [])
  for episode in sorted(
    episodes,
    key = lambda episode: episode[sort_field]):
    yield episode


def retrieve_sorted_movies(rpc, sort_field='movieid', filters=None):
  """rpc should be a callable which will send the JSONRPC request to the Kodi server"""
  episodes =  rpc(list_movies(tv_show_id)).get('movies', [])
  for episode in sorted(
    episodes,
    key = lambda episode: episode[sort_field]):
    yield episode


def retrieve_sorted_shows(rpc, tv_show_id = None, sort_field='tvshowid', filters=None):
  """rpc should be a callable which will send the JSONRPC request to the Kodi server. tv_show_id can be used to restrict the list to a single id."""
  shows = rpc(list_tv_shows()).get('tvshows',[])
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
  fields should be a list of tuples (str,int): (field_name, length)  
  """
  for item in items:
    for (field_name, length) in fields:
      if type(item[field_name]) is str or type(item[field_name]) is unicode:
        field_value = item[field_name]
      else:
        field_value = str(item[field_name])
      item['display{0}'.format(field_name)] = field_value[0:length-1].ljust(length)
  return items
