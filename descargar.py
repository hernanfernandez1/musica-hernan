"""
StemGame v3 — 150 canciones
Ejecuta: py -3.11 descargar.py
"""
import subprocess, sys, os, json, re, glob

def instalar(pkg, imp=None):
    try: __import__(imp or pkg.replace("-","_"))
    except ImportError:
        print(f"  Instalando {pkg}...")
        subprocess.check_call([sys.executable,"-m","pip","install",pkg,"-q"])

print("\n" + "="*54)
print("  StemGame v3 — 150 canciones")
print("="*54 + "\n")
instalar("yt-dlp","yt_dlp")
instalar("demucs")
instalar("imageio-ffmpeg","imageio_ffmpeg")

import imageio_ffmpeg
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)
local_dir  = os.getcwd()
env = os.environ.copy()
env["PATH"] = local_dir + os.pathsep + ffmpeg_dir + os.pathsep + env.get("PATH","")

print("FFmpeg listo\n")
input("Presiona Enter para empezar...")
print()

CANCIONES = {
    "2000s": [
        {"titulo":"Crazy in Love","artista":"Beyonce","año":2003},
        {"titulo":"Yeah","artista":"Usher","año":2004},
        {"titulo":"In Da Club","artista":"50 Cent","año":2003},
        {"titulo":"Boulevard of Broken Dreams","artista":"Green Day","año":2004},
        {"titulo":"Mr Brightside","artista":"The Killers","año":2003},
        {"titulo":"Hey Ya","artista":"OutKast","año":2003},
        {"titulo":"Clocks","artista":"Coldplay","año":2002},
        {"titulo":"Since U Been Gone","artista":"Kelly Clarkson","año":2004},
        {"titulo":"Lose Yourself","artista":"Eminem","año":2002},
        {"titulo":"Beautiful Day","artista":"U2","año":2000},
        {"titulo":"Numb","artista":"Linkin Park","año":2003},
        {"titulo":"In the End","artista":"Linkin Park","año":2001},
        {"titulo":"Seven Nation Army","artista":"The White Stripes","año":2003},
        {"titulo":"Toxic","artista":"Britney Spears","año":2003},
        {"titulo":"Complicated","artista":"Avril Lavigne","año":2002},
        {"titulo":"Sk8er Boi","artista":"Avril Lavigne","año":2002},
        {"titulo":"Umbrella","artista":"Rihanna","año":2007},
        {"titulo":"Beautiful","artista":"Christina Aguilera","año":2002},
        {"titulo":"This Love","artista":"Maroon 5","año":2004},
        {"titulo":"Feel Good Inc","artista":"Gorillaz","año":2005},
        {"titulo":"Hips Don't Lie","artista":"Shakira","año":2006},
        {"titulo":"Gold Digger","artista":"Kanye West","año":2005},
        {"titulo":"Hollaback Girl","artista":"Gwen Stefani","año":2004},
        {"titulo":"Fix You","artista":"Coldplay","año":2005},
        {"titulo":"La Camisa Negra","artista":"Juanes","año":2004},
        {"titulo":"A Dios Le Pido","artista":"Juanes","año":2002},
        {"titulo":"Inevitable","artista":"Shakira","año":2001},
        {"titulo":"Livin la Vida Loca","artista":"Ricky Martin","año":1999},
        {"titulo":"Gasolina","artista":"Daddy Yankee","año":2004},
        {"titulo":"Lo Que Paso Paso","artista":"Daddy Yankee","año":2004},
    ],
    "2010s": [
        {"titulo":"Rolling in the Deep","artista":"Adele","año":2010},
        {"titulo":"Uptown Funk","artista":"Mark Ronson","año":2014},
        {"titulo":"Shape of You","artista":"Ed Sheeran","año":2017},
        {"titulo":"Happy","artista":"Pharrell Williams","año":2013},
        {"titulo":"Chandelier","artista":"Sia","año":2014},
        {"titulo":"Get Lucky","artista":"Daft Punk","año":2013},
        {"titulo":"Royals","artista":"Lorde","año":2013},
        {"titulo":"Someone Like You","artista":"Adele","año":2011},
        {"titulo":"Shallow","artista":"Lady Gaga","año":2018},
        {"titulo":"Thinking Out Loud","artista":"Ed Sheeran","año":2014},
        {"titulo":"Stay With Me","artista":"Sam Smith","año":2014},
        {"titulo":"Take Me to Church","artista":"Hozier","año":2013},
        {"titulo":"Shake It Off","artista":"Taylor Swift","año":2014},
        {"titulo":"Can't Stop the Feeling","artista":"Justin Timberlake","año":2016},
        {"titulo":"Stressed Out","artista":"Twenty One Pilots","año":2015},
        {"titulo":"Closer","artista":"The Chainsmokers","año":2016},
        {"titulo":"Despacito","artista":"Luis Fonsi","año":2017},
        {"titulo":"Mi Gente","artista":"J Balvin","año":2017},
        {"titulo":"Love Yourself","artista":"Justin Bieber","año":2015},
        {"titulo":"Sorry","artista":"Justin Bieber","año":2015},
        {"titulo":"Havana","artista":"Camila Cabello","año":2017},
        {"titulo":"Perfect","artista":"Ed Sheeran","año":2017},
        {"titulo":"Thunder","artista":"Imagine Dragons","año":2017},
        {"titulo":"Believer","artista":"Imagine Dragons","año":2017},
        {"titulo":"Propuesta Indecente","artista":"Romeo Santos","año":2013},
        {"titulo":"Darte un Beso","artista":"Prince Royce","año":2012},
        {"titulo":"Me Rehuso","artista":"Danny Ocean","año":2016},
        {"titulo":"Waka Waka","artista":"Shakira","año":2010},
        {"titulo":"Chantaje","artista":"Shakira","año":2016},
        {"titulo":"Con Calma","artista":"Daddy Yankee","año":2019},
    ],
    "2020s": [
        {"titulo":"Blinding Lights","artista":"The Weeknd","año":2020},
        {"titulo":"Levitating","artista":"Dua Lipa","año":2020},
        {"titulo":"drivers license","artista":"Olivia Rodrigo","año":2021},
        {"titulo":"Stay","artista":"The Kid LAROI","año":2021},
        {"titulo":"As It Was","artista":"Harry Styles","año":2022},
        {"titulo":"Anti-Hero","artista":"Taylor Swift","año":2022},
        {"titulo":"Flowers","artista":"Miley Cyrus","año":2023},
        {"titulo":"Unholy","artista":"Sam Smith","año":2022},
        {"titulo":"Heat Waves","artista":"Glass Animals","año":2020},
        {"titulo":"Bad Habit","artista":"Steve Lacy","año":2022},
        {"titulo":"good 4 u","artista":"Olivia Rodrigo","año":2021},
        {"titulo":"Montero","artista":"Lil Nas X","año":2021},
        {"titulo":"Save Your Tears","artista":"The Weeknd","año":2021},
        {"titulo":"Easy On Me","artista":"Adele","año":2021},
        {"titulo":"Golden Hour","artista":"JVKE","año":2022},
        {"titulo":"Cruel Summer","artista":"Taylor Swift","año":2019},
        {"titulo":"Dynamite","artista":"BTS","año":2020},
        {"titulo":"Butter","artista":"BTS","año":2021},
        {"titulo":"Running Up That Hill","artista":"Kate Bush","año":2022},
        {"titulo":"Physical","artista":"Dua Lipa","año":2020},
        {"titulo":"Dakiti","artista":"Bad Bunny","año":2020},
        {"titulo":"Titi Me Pregunto","artista":"Bad Bunny","año":2022},
        {"titulo":"Me Porto Bonito","artista":"Bad Bunny","año":2022},
        {"titulo":"Ojitos Lindos","artista":"Bad Bunny","año":2022},
        {"titulo":"Efecto","artista":"Bad Bunny","año":2022},
        {"titulo":"Provenza","artista":"Karol G","año":2022},
        {"titulo":"Tusa","artista":"Karol G","año":2019},
        {"titulo":"Gatubela","artista":"Karol G","año":2022},
        {"titulo":"Quevedo Bzrp Session 52","artista":"Bizarrap","año":2022},
        {"titulo":"Despecha","artista":"Rosalia","año":2022},
    ],
}

def slug(a, t):
    s = f"{a}_{t}".lower().replace(" ","_")
    return re.sub(r"[^a-z0-9_]","",s)

os.makedirs("audio_raw", exist_ok=True)

# Cargar songs.json existente
try:
    with open("songs.json","r",encoding="utf-8") as f:
        songs_data = json.load(f)
    print(f"Songs.json existente: {len(songs_data)} canciones\n")
except:
    songs_data = []

# Set de canciones ya procesadas
procesadas = {(s["titulo"].lower(), s["artista"].lower()) for s in songs_data}

total = sum(len(v) for v in CANCIONES.values())
n = 0
nuevas = 0

for decada, lista in CANCIONES.items():
    print(f"\n{'─'*54}\n  {decada}\n{'─'*54}")

    for song in lista:
        n += 1
        sl    = slug(song["artista"], song["titulo"])
        query = f"{song['titulo']} {song['artista']} audio"

        print(f"\n[{n}/{total}] {song['titulo']} - {song['artista']}")

        # Saltear si ya está procesada
        if (song["titulo"].lower(), song["artista"].lower()) in procesadas:
            print("  Ya procesada, salteando")
            continue

        archivos = glob.glob(f"audio_raw/{sl}.*")
        mp3 = archivos[0] if archivos else None

        if not mp3:
            print("  Descargando de YouTube...")
            cmd = [
                sys.executable, "-m", "yt_dlp",
                f"ytsearch1:{query}",
                "--no-playlist", "-x",
                "--audio-format", "mp3",
                "--audio-quality", "192K",
                "--ffmpeg-location", local_dir,
                "-o", f"audio_raw/{sl}.%(ext)s",
                "--no-warnings", "-q",
                "--postprocessor-args", "ffmpeg:-ss 15 -t 35",
            ]
            subprocess.run(cmd, env=env)
            archivos = glob.glob(f"audio_raw/{sl}.*")
            if not archivos:
                print("  ERROR al descargar, salteando")
                continue
            mp3 = archivos[0]
            print(f"  OK - {os.path.basename(mp3)}")
        else:
            print(f"  Audio existe: {os.path.basename(mp3)}")

        base       = os.path.splitext(os.path.basename(mp3))[0]
        stem_dir   = os.path.join("separated", "htdemucs", base)
        drums_path = os.path.join(stem_dir, "drums.mp3")

        if not os.path.exists(drums_path):
            print("  Separando con IA...")
            r = subprocess.run(
                [sys.executable, "-m", "demucs", "--mp3", "-n", "htdemucs", mp3],
                capture_output=True, text=True, env=env
            )
            if os.path.exists(drums_path):
                print("  OK - bateria / bajo / melodia / voz")
            else:
                print("  ERROR en Demucs")
                print(f"  {r.stderr[-300:]}")
                continue
        else:
            print("  Stems ya existen")

        songs_data.append({
            "titulo":  song["titulo"],
            "artista": song["artista"],
            "año":     song["año"],
            "decada":  decada,
            "stems": {
                "drums":  f"separated/htdemucs/{base}/drums.mp3",
                "bass":   f"separated/htdemucs/{base}/bass.mp3",
                "other":  f"separated/htdemucs/{base}/other.mp3",
                "vocals": f"separated/htdemucs/{base}/vocals.mp3",
            }
        })
        procesadas.add((song["titulo"].lower(), song["artista"].lower()))
        nuevas += 1

        with open("songs.json","w",encoding="utf-8") as f:
            json.dump(songs_data, f, ensure_ascii=False, indent=2)

print(f"\n{'='*54}")
print(f"  LISTO: {len(songs_data)} canciones totales ({nuevas} nuevas)")
print(f"{'='*54}\n")
print("Para subir a GitHub:")
print('  D:\\PortableGit\\bin\\git.exe add .')
print('  D:\\PortableGit\\bin\\git.exe commit -m "canciones nuevas"')
print('  D:\\PortableGit\\bin\\git.exe push\n')
