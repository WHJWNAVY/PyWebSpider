# 准备工作

## requests安装

```bash
pip install requests
```

> 需要管理员权限



## lxml安装

```bash
pip install lxml
```

> 需要管理员权限



## selenium安装

```bash
pip install selenium
```

> 需要管理员权限

### [Selenium Driver](https://selenium-python.readthedocs.io/installation.html#drivers)

| **Browser** | Download Link |
| :------: | ---------- |
| **Chrome** |  <https://sites.google.com/a/chromium.org/chromedriver/downloads> |
| **Edge** | <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/> |
| **Firefox** | <https://github.com/mozilla/geckodriver/releases>|
| **Safari** | <https://webkit.org/blog/6900/webdriver-support-in-safari-10/> |

例如: [chromedriver_win32_80.0.3987.106.zip](https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_win32.zip)

> * 找到与你的Chrome浏览器版本对应的ChromeDriver
>
> * 下载后解压到指定文件夹，例如 `D:\Program Files (x86)\ChromeDriver\chromedriver.exe`
> * 把ChromeDriver文件夹加入到环境变量中，例如 `D:\Program Files (x86)\ChromeDriver`
> * `此电脑->右键->属性->高级系统设置->环境变量->PATH->编辑`



# 喜马拉雅下载

## 获取专辑信息

### URL

```http
https://www.ximalaya.com/revision/album?albumId=9742789
```

### HEAD

```http
Host: www.ximalaya.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,en-US;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Cookie: _xmLog=xm_k3y398c7i05jvx; device_id=xm_1575874949738_k3y399bezjz1wg; 1&remember_me=y; 1&_token=33137912&FF000ABB23B848DBA185E16B631D2DF5NdVE12943B8C0EBB477803F032FA8A489EDC16D751007A6314F14EFABE75DD5DFD1; s&e=e7046fac04d436894cbdd17a6a8743e8; s&a=%1FP_WT%09%1A%04J_%0BWYYCZN%0C%09%07%0AR@%02@%0AWXZT%1E[VPCTBVLOKRYSBW@X; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A
Upgrade-Insecure-Requests: 1
```

### PAYLOAD

```json
{
    "ret": 200,
    "msg": "成功",
    "data": {
        "isSelfAlbum": false,
        "currentUid": 33137912,
        "albumId": 9742789,
        "mainInfo": {
            "albumStatus": 1,
            "showApplyFinishBtn": false,
            "showEditBtn": false,
            "showTrackManagerBtn": false,
            "showInformBtn": true,
            "cover": "//imagev2.xmcdn.com/group69/M01/51/D8/wKgMeV3L1dizfiHjAAC_6wnqGFY23.jpeg",
            "albumTitle": "郭德纲高清相声集【精选】",
            "crumbs": {
                "categoryId": 12,
                "categoryPinyin": "xiangsheng",
                "categoryTitle": "相声评书",
                "subcategoryId": 20,
                "subcategoryName": "相声",
                "subcategoryDisplayName": "相声",
                "subcategoryCode": "xiangsheng"
            },
            "updateDate": "2020-04-01",
            "createDate": "2017-08-02",
            "playCount": 368527505,
            "isPaid": false,
            "isFinished": 1,
            "metas": [
                {
                    "metaValueId": 1684,
                    "metaDataId": 108,
                    "categoryId": 12,
                    "isSubCategory": false,
                    "categoryName": "xiangsheng",
                    "categoryPinyin": "xiangsheng",
                    "metaValueCode": "guodegang",
                    "metaDisplayName": "郭德纲",
                    "link": "/xiangsheng/xiangsheng/mr108t1684/"
                },
                {
                    "metaValueId": 18,
                    "metaDataId": 47,
                    "categoryId": 12,
                    "isSubCategory": false,
                    "categoryName": "xiangsheng",
                    "categoryPinyin": "xiangsheng",
                    "metaValueCode": "duikou",
                    "metaDisplayName": "对口",
                    "link": "/xiangsheng/xiangsheng/mr47t18/"
                },
            ],
            "isSubscribe": true,
            "richIntro": "",
            "shortIntro": "",
            "detailRichIntro": "",
            "isPublic": true,
            "hasBuy": false,
            "vipType": 0,
            "canCopyText": true,
            "subscribeCount": 1200469,
            "sellingPoint": {},
            "personalDescription": "",
            "bigshotRecommend": "",
            "outline": "<p style=\"line-height:30px;hyphens:auto;color:#333333;text-align:left;font-size:16px;font-family:Helvetica,Arial,sans-serif;font-weight:normal\" data-flag=\"normal\">郭德纲高清相声集，喜马独家音频放送</p>",
            "customTitle": "",
            "produceTeam": "",
            "recommendReason": "郭德纲献给老司机们的福利，不可错过"
        },
        "anchorInfo": {
            "anchorId": 1000202,
            "anchorCover": "//imagev2.xmcdn.com/group1/M00/0B/3D/wKgDrlESHqyTqakZAADewk1yMt8360.jpg",
            "showFollowBtn": false,
            "anchorName": "德云社郭德纲相声VIP",
            "anchorGrade": 16,
            "anchorGradeType": 2,
            "anchorAlbumsCount": 95,
            "anchorTracksCount": 4772,
            "anchorFollowsCount": 9,
            "anchorFansCount": 13625314,
            "personalIntroduction": "郭德纲领衔德云社唯一授权音频平台。郭德纲相声，包括其著名的君臣斗、马寿出世、宋金刚押宝、解学士等。",
            "showAnchorAlbumModel": true,
            "anchorAlbumList": [
                {
                    "albumId": 35825497,
                    "albumTitle": "德云社20周年闭幕庆典 2017",
                    "cover": "//imagev2.xmcdn.com/group78/M06/13/37/wKgO4F57GOHh4sHOAAuseqOKTow064.jpg",
                    "playCount": 283972,
                    "tracksCount": 6,
                    "anchorId": 1000202,
                    "anchorName": "德云社郭德纲相声VIP",
                    "url": "/xiangsheng/35825497/"
                },
                {
                    "albumId": 35200768,
                    "albumTitle": "郭德纲相声专场 熊本站2017",
                    "cover": "//imagev2.xmcdn.com/group74/M09/30/EF/wKgO0l5rKwuwXxIzAAeRgVnaH9E885.jpg",
                    "playCount": 1108877,
                    "tracksCount": 6,
                    "anchorId": 1000202,
                    "anchorName": "德云社郭德纲相声VIP",
                    "url": "/xiangsheng/35200768/"
                }
            ],
            "hasMoreBtn": true,
            "logoType": 4
        },
        "tracksInfo": {
            "trackTotalCount": 129,
            "sort": 0,
            "tracks": [
                {
                    "index": 1,
                    "trackId": 46430558,
                    "isPaid": false,
                    "tag": 0,
                    "title": "郭德纲《学徒艰辛》老郭打磕巴了，罕见",
                    "playCount": 18845946,
                    "showLikeBtn": true,
                    "isLike": false,
                    "showShareBtn": true,
                    "showCommentBtn": true,
                    "showForwardBtn": true,
                    "createDateFormat": "2年前",
                    "url": "/xiangsheng/9742789/46430558",
                    "duration": 1993,
                    "isVideo": false,
                    "videoCover": null,
                    "isVipFirst": false,
                    "breakSecond": 0,
                    "length": 1993
                },
                {
                    "index": 30,
                    "trackId": 46219386,
                    "isPaid": false,
                    "tag": 0,
                    "title": "郭德纲《于谦相亲被强吻》皮条胡同拉家",
                    "playCount": 2859168,
                    "showLikeBtn": true,
                    "isLike": false,
                    "showShareBtn": true,
                    "showCommentBtn": true,
                    "showForwardBtn": true,
                    "createDateFormat": "2年前",
                    "url": "/xiangsheng/9742789/46219386",
                    "duration": 1480,
                    "isVideo": false,
                    "videoCover": null,
                    "isVipFirst": false,
                    "breakSecond": 0,
                    "length": 1480
                }
            ],
            "pageNum": 1,
            "pageSize": 30,
            "lastPlayTrackId": 46219230
        },
        "subSiteAlbumUrl": "",
        "recommendKw": {
            "sourceKw": "郭德纲高清相声集【精选】",
            "recommendText": [
                "听云鹏的相声",
                "单田芳水浒",
                "郭德纲相声超清",
                "郭德纲于谦高清相声"
            ]
        },
        "draft": null,
        "isTemporaryVIP": false
    }
}
```



## 获取专辑列表

### URL

```http
https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=9742789&pageNum=1&pageSize=1000
```

### HEAD

```http
Host: www.ximalaya.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,en-US;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Cookie: _xmLog=xm_k3y398c7i05jvx; device_id=xm_1575874949738_k3y399bezjz1wg; 1&remember_me=y; 1&_token=33137912&FF000ABB23B848DBA185E16B631D2DF5NdVE12943B8C0EBB477803F032FA8A489EDC16D751007A6314F14EFABE75DD5DFD1; s&e=e7046fac04d436894cbdd17a6a8743e8; s&a=%1FP_WT%09%1A%04J_%0BWYYCZN%0C%09%07%0AR@%02@%0AWXZT%1E[VZ_OXOB[VZVU^OBWN; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0, no-cache
TE: Trailers
Pragma: no-cache
```

### PAYLOAD

```json
{
    "ret": 200,
    "data": {
        "currentUid": 33137912,
        "albumId": 9742789,
        "trackTotalCount": 129,
        "sort": 0,
        "tracks": [
            {
                "index": 1,
                "trackId": 46430558,
                "isPaid": false,
                "tag": 0,
                "title": "郭德纲《学徒艰辛》老郭打磕巴了，罕见",
                "playCount": 18826557,
                "showLikeBtn": true,
                "isLike": false,
                "showShareBtn": true,
                "showCommentBtn": true,
                "showForwardBtn": true,
                "createDateFormat": "2年前",
                "url": "/xiangsheng/9742789/46430558",
                "duration": 1993,
                "isVideo": false,
                "videoCover": null,
                "isVipFirst": false,
                "breakSecond": 742,
                "length": 1993
            },
            {
                "index": 2,
                "trackId": 46430560,
                "isPaid": false,
                "tag": 0,
                "title": "郭德纲《三米高的马桶》上厕所靠重力",
                "playCount": 18212042,
                "showLikeBtn": true,
                "isLike": false,
                "showShareBtn": true,
                "showCommentBtn": true,
                "showForwardBtn": true,
                "createDateFormat": "2年前",
                "url": "/xiangsheng/9742789/46430560",
                "duration": 1898,
                "isVideo": false,
                "videoCover": null,
                "isVipFirst": false,
                "breakSecond": 0,
                "length": 1898
            },
            {
                "index": 3,
                "trackId": 46430562,
                "isPaid": false,
                "tag": 0,
                "title": "郭德纲 《京中名妓》你先应付着",
                "playCount": 13770315,
                "showLikeBtn": true,
                "isLike": false,
                "showShareBtn": true,
                "showCommentBtn": true,
                "showForwardBtn": true,
                "createDateFormat": "2年前",
                "url": "/xiangsheng/9742789/46430562",
                "duration": 1683,
                "isVideo": false,
                "videoCover": null,
                "isVipFirst": false,
                "breakSecond": 0,
                "length": 1683
            }
        ],
        "pageNum": 1,
        "pageSize": 3,
        "superior": [],
        "lastPlayTrackId": 46430558
    }
}
```



## 获取播放文件

### URL

```http
https://www.ximalaya.com/revision/play/v1/audio?id=46430558&ptype=1
```

### HEAD

```http
Host: www.ximalaya.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,en-US;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Cookie: _xmLog=xm_k3y398c7i05jvx; device_id=xm_1575874949738_k3y399bezjz1wg; 1&remember_me=y; 1&_token=33137912&FF000ABB23B848DBA185E16B631D2DF5NdVE12943B8C0EBB477803F032FA8A489EDC16D751007A6314F14EFABE75DD5DFD1; s&e=e7046fac04d436894cbdd17a6a8743e8; s&a=%1FP_WT%09%1A%04J_%0BWYYCZN%0C%09%07%0AR@%02@%0AWXZT%1E[VZCSBRMOKRYSBZOW; x_xmly_traffic=utm_source%253A%2526utm_medium%253A%2526utm_campaign%253A%2526utm_content%253A%2526utm_term%253A%2526utm_from%253A
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
TE: Trailers
```

### PAYLOAD

```json
{
    "ret": 200,
    "data": {
        "trackId": 46430558,
        "canPlay": true,
        "isPaid": false,
        "hasBuy": true,
        "src": "https://fdfs.xmcdn.com/group31/M0B/6C/F8/wKgJX1mG0xDCFUfeAPYI4CGwxyI618.m4a",
        "albumIsSample": false,
        "sampleDuration": 0,
        "isBaiduMusic": false,
        "firstPlayStatus": true
    }
}
```

