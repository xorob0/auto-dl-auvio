# Auto DL Auvio

This container is my way of automatically download videos from [Auvio](https://auvio.be). You give it the link to your TV show, a system path and a delay and it will automatically download new episodes.

You can run it with this command:
```
 docker run -v /video/demain:/output -e url="https://www.rtbf.be/auvio/emissions/detail_demain-nous-appartient?id=11520" -e timeout=3600 -e path=/output xorob00/auto-dl-auvio
```

## Disclamer
I'm not a Python dev, this code works for me but it might not do what you want. If you have feature request just drop me an issue and I'll try to see what I can do.