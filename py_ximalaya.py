import WebSpider as WS
import json

USE_BROWSER = True
BROWSER_NAME = "Edge"

ALBUM_INFO_URL_FMT="https://www.ximalaya.com/revision/album?albumId={0}"
ALBUM_LIST_URL_FMT="https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={0}&pageNum=1&pageSize=1000"
TRACK_INFO_URL_FMT="https://www.ximalaya.com/revision/play/v1/audio?id={0}&ptype=1"

def xmly_ws_filter_json(html):
    album_info_html = html
    if USE_BROWSER == True:
        if BROWSER_NAME == "Edge":
            album_info_html = ws.FilterHtml(album_info_html, "/html/body/pre/text()")
        elif BROWSER_NAME == "Firefox":
            album_info_html = ws.FilterHtml(album_info_html, "/html/body/div/div/text()")
        album_info_html = album_info_html[0]

    return album_info_html

def xmly_get_album_info(ws, album_id):
    album_info_url = ALBUM_INFO_URL_FMT.format(album_id)
    print("Album Info Url: {0}".format(album_info_url))
    album_info_html = ws.Gethtml(album_info_url)
    if album_info_html == None:
        print("Fail to get album info!")
        return None
    # print(album_info_html)

    album_info_json = xmly_ws_filter_json(album_info_html)

    album_info_json = json.loads(album_info_json)
    # print(album_info_json)

    if album_info_json == None:
        print("Invalid Album Info Json!")
        return None

    album_info_data = album_info_json["data"]

    albumTitle = album_info_data["mainInfo"]["albumTitle"]
    print("albumTitle: {0}".format(albumTitle))

    albumCover = album_info_data["mainInfo"]["cover"]
    albumCover = "http:{0}".format(albumCover)
    print("albumCover: {0}".format(albumCover))

    return albumTitle, albumCover

def xmly_get_track_info(ws, track_id):
    track_info_url = TRACK_INFO_URL_FMT.format(track_id)
    print("Tracks Info Url: {0}".format(track_info_url))
    track_info_html = ws.Gethtml(track_info_url)
    if track_info_html == None:
        print("Fail to get track info!")
        return None
    # print(track_info_html)

    track_info_json = xmly_ws_filter_json(track_info_html)

    track_info_json = json.loads(track_info_json)
    # print(track_info_json)
    
    if track_info_json == None:
        print("Invalid Track Info Json!")
        return None

    track_info_data = track_info_json["data"]

    track_file_url = track_info_data["src"]
    print("Track File Url: {0}".format(track_file_url))

    return track_file_url

def xmly_get_album_list(ws, album_id):
    album_list_url = ALBUM_LIST_URL_FMT.format(album_id)
    print("Album List Url: {0}".format(album_list_url))
    album_list_html = ws.Gethtml(album_list_url)
    if album_list_html == None:
        print("Fail to get album info!")
        return None
    # print(album_list_html)

    album_list_json = xmly_ws_filter_json(album_list_html)

    album_list_json = json.loads(album_list_json)
    # print(album_list_json)

    if album_list_json == None:
        print("Invalid Album List Json!")
        return None

    album_list_data = album_list_json["data"]

    print("albumId = {0}".format(album_list_data["albumId"]))
    print("trackTotalCount = {0}".format(album_list_data["trackTotalCount"]))

    tracks_list_data = album_list_data["tracks"]

    tracks_list_ret = []
    for t in tracks_list_data:
        tracks_data_list = []
        tracks_data_list.append(t["index"])     # 0
        tracks_data_list.append(t["trackId"])   # 1
        tracks_data_list.append(t["title"])     # 2
        tracks_data_list.append(t["url"])       # 3

        track_file_url = xmly_get_track_info(ws, t["trackId"])
        tracks_data_list.append(track_file_url) # 4

        print(tracks_data_list)
        tracks_list_ret.append(tracks_data_list)
        # ws.Wait()

    # print(tracks_list_ret)
    return tracks_list_ret

if __name__ == "__main__":
    album_id = input("Please Input Album ID:")
    if album_id == None or len(album_id) == 0:
        print("Invalid Album ID!")
        exit(0)

    ws = WS.WebSpider(use_browser=USE_BROWSER, browser=BROWSER_NAME)
    # print(ws.WebHeader["Accept"])
    # print(ws.WebHeader["User-Agent"])
    
    album_title, album_cover = xmly_get_album_info(ws, album_id)
    album_tracks_list = xmly_get_album_list(ws, album_id)
    
    csv_file_name = album_title
    # csv_file_name = "auto"
    
    for at in album_tracks_list:
        ws.Save(at, csv_file_name)
        save_file_path = at[4]
        save_file_name = "{0}.m4a".format(at[2])
        print("Download file [{0}] ...".format(save_file_name))
        ws.GetFile(save_file_path, album_title, save_file_name)
        # ws.Wait()
