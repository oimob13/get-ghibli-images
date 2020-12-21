import subprocess

titles = {
    'red-turtle' : 28,
    'onyourmark' : 50,
    'omoide' : 50,
    'laputa' : 50,
    'nausicaa' : 50,
    'tanuki' : 50,
    'umi' : 50,
    'porco' : 50,
    'majo' : 50,
    'totoro' : 50,
    'howl' : 50,
    'baron' : 50,
    'ghiblies' : 50,
    'yamada' : 50,
    'mononoke' : 50,
    'mimi' : 50,
    'marnie' : 50,
    'kaguyahime' : 50,
    'kazetachinu' : 50,
    'kokurikozaka' : 50,
    'karigurashi' : 50,
    'ponyo' : 50,
    'ged' : 50,
    'chihiro' : 50,
}


for key, val in titles.items():
    for i in range(1, val + 1):
        url = "https://www.ghibli.jp/gallery/{0}{1:03d}.jpg".format(key, i)
        subprocess.run(["curl", "-O", url])
