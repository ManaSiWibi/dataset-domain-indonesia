Pembaharuan terakhir: 17/11/23


# Kumpulan Dataset Domain Indonesia
Repository ini merupakan kumpulan domain atau situs website dengan TLD maupun ccTLD di Indonesia.

# Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation
Metodologi: https://tranco-list.eu/methodology  
lines: 26166
```
$ curl -O -J -L https://tranco-list.eu/download/Z257G/full 
$ cut -d, -f1 --complement tranco_Z257G.csv > domain.txt
$ grep -E "\.id[[:space:]]$" domain.txt > domains.txt

```

# ipsniper
| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id         | 98953             |
| 2  | .co.id      | 61372             |
| 3  | .my.id      | 56816             |
| 4  | .sch.id     | 30219             |
| 5  | .web.id     | 10941             |
| 6  | .desa.id    | 8829              |
| 7  | .or.id      | 7921              |
| 8  | .ac.id      | 5111              |
| 9  | .biz.id     | 2257              |
| 10 | .go.id      | 2063              |
| 11 | .net.id     | 605               |
| 12 | .ponpes.id  | 457               |
| 13 | .mil.id     | 124               |
|  Total  |        | 285668            |


### Sampel
```
stkipahsingaraja.ac.id
pn-pariaman.go.id
riso.id
korem082.mil.id
rumput.or.id
```

# Domains Project
Metodologi: https://github.com/tb0hdan/domains#crawlers  
lines: 2544669


| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .co.id      | 640060(?)            |
| 2  | .id         | 633676            |
| 3  | .sch.id     | 261613            |
| 4  | .my.id      | 255246            |
| 5  | .ac.id      | 211128            |
| 6  | .net.id     | 162544            |
| 7  | .go.id      | 157987            |
| 8  | .web.id     | 111413            |
| 9  | .or.id      | 65518             |
| 10 | .desa.id    | 30443             |
| 11 | .biz.id     | 10383             |
| 12 | .ponpes.id  | 3451              |
| 13 | .mil.id     | 1207              |
|   Total |        | 2544669           |


### Sampel
```
backup.poltekim.ac.id
mx.cahayabarumulia.co.id
sdnegeri16bandarrahmad.sch.id
www.langitpayment.web.id
cpanel.globaltrade.co.id
```

# Sumber
https://domainsproject.org/

https://ipsniper.info/