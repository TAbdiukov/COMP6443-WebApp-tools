# WebApp-tools
Tools designed to help pass the UNSW's COMP6443 / 6483 course (WebApp security)

Course code isn't in the repo name to prevent 'dumb' fetching the repo

## Trivia
All things here were written ASAP upon the need with the lack of optimisation

* **Misc** - Things I were working on but never got time to finish
* **bruteGetIPs** - brutes the IP addresses on the dns ns.agency website. Takes one argument, the URL
* **bruteBing** - brutes the ns.agency's pastebin knockoff on pastebing.ns.agency for the pastes encoded via Base62 scheme.  Takes two arguments, the URL and the number of (remaining) base62 places to brute
* **gent** - generates text wiithin the range and copies it to clipboard (for the future use)
* **intelBing** - a not-so successful attempt on gathering pastebing logic information by spamming pastes
* 🚗**peekRive** - dumps bing drive pastes via peeker-seeker
* 🚗**peekRive_reverse** - reverse-dumps bing drive by reverse user lookup from classic peekRive

## Third party useful stuff
### Scripts
* [git-dumper](https://github.com/arthaud/git-dumper) - Dumps .git directories where present. Helpt me greatly a couple of times
* [dnsrecon](https://github.com/darkoperator/dnsrecon) - DNS subdomain bruteforcer
* [clone-gists.py](https://gist.github.com/SpotlightKid/042491a9a2987af04a5a) - Dump someone's all dists via API
* [primefac fork](https://github.com/elliptic-shiho/primefac-fork) - VERY Fast prime factorisation. Use -v flag

### Apps
* [Nmap](https://nmap.org/) - Port scanning and service pentesting tool
* [sqlmap](http://sqlmap.org/) - I'll kill you all! In the sequel!
* [Burp](https://portswigger.net/burp/communitydownload) - Intercept all traffic w/o messing with WireShark
* [WireShark](https://www.wireshark.org/) - Low-level packet analytics tool
* [Tor](https://www.torproject.org) - Humanity's worst challenger
* [kitty](http://kitty.9bis.net/) - great fork of putty

### Browser extensions
#### Official
* [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) - Edit Chrome cookies
* [Cookie Editor](https://addons.mozilla.org/en-US/firefox/addon/edit-cookie/) - Edit Firefox cookies

* [Proxy SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif/related) - Force Chrome to use proxy
* [Proxy SwitchyOmega](https://addons.mozilla.org/en-US/firefox/addon/switchyomega/) - Force Firefox to use proxy

#### Unofficial
* [View Page Archive & Cache](https://github.com/dessant/view-page-archive) - Check if any online archive would leak anything worthy (Chrome, Firefox, Opera)
* [Violentmonkey](https://violentmonkey.github.io/) - Violent user scripts in your browser

### SAAS's
* [CentralOps](https://centralops.net/co/) - Online DNS and WHOIS lookup tools
* [IpLocation](https://www.iplocation.net/) - IP location
* [NIC](https://www.nic.ru/whois/?searchWord=put_url_here) - Russian WHOIS service. May produce different results as the authoritaristic DNS alternative emerges
* [dencoder](https://meyerweb.com/eric/tools/dencoder/) - URL encoder and decoder
* [dcode.fr](https://www.dcode.fr/base-n-convert) - 6441 stuff hate him! Because of this one simplec trick!

### Docs to see
* [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Swiss army knife for injections and what not

### Leaked data
* [9k](9k) - kill the Windows 98 
* [Flask core](https://github.com/secedu/flask-core) - core used by COMP6443

## Things I look for
* Executable arguments' blind but smart bruteforcer (both Linux and Windows)
* ~~Cheat engine for Linux~~ Direct access via /proc folder
* ~~AHK for linux~~ [archive.org](https://web.archive.org/web/20190324162541/https://unix.stackexchange.com/questions/165124/autohotkey-equivalent)
* WinHex analytics bundles for linux

## May I contribute?
Please do 