Pembaharuan terakhir: 17/05/26


# Kumpulan Dataset Domain Indonesia
Repository ini merupakan kumpulan domain atau situs website dengan TLD maupun ccTLD di Indonesia.

# Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation
Metodologi: https://tranco-list.eu/methodology
List ID: 43KLX (2026-05-16)
lines: 11220
```
$ curl -O -J -L https://tranco-list.eu/download/43KLX/full
$ tr -d '\r' < tranco_43KLX_full.csv | awk -F',' '{print $2}' | grep '\.id$' > domains.txt

```

| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id (pure)  | 4567              |
| 2  | .co.id      | 2589              |
| 3  | .ac.id      | 1609              |
| 4  | .go.id      | 931               |
| 5  | .my.id      | 354               |
| 6  | .sch.id     | 317               |
| 7  | .net.id     | 414               |
| 8  | .web.id     | 180               |
| 9  | .or.id      | 138               |
| 10 | .biz.id     | 101               |
| 11 | .desa.id    | 9                 |
| 12 | .mil.id     | 10                |
| 13 | .ponpes.id  | 1                 |
|   Total |        | 11220             |

# ipsniper
| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id         | 1259315           |
| 2  | .my.id      | 991174            |
| 3  | .co.id      | 485369            |
| 4  | .biz.id     | 316438            |
| 5  | .web.id     | 304547            |
| 6  | .sch.id     | 218977            |
| 7  | .or.id      | 71545             |
| 8  | .desa.id    | 60351             |
| 9  | .ac.id      | 50742             |
| 10 | .go.id      | 13269             |
| 11 | .net.id     | 5011              |
| 12 | .ponpes.id  | 6184              |
| 13 | .mil.id     | 547               |
| 14 | .xn--9tfky.id | 38               |
| 15 | .kop.id     | 28                |
|  Total  |        | 3783524           |


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
Source: https://domainsproject.org/
lines: 2544669


| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .co.id      | 639898            |
| 2  | .id (pure)  | 118191            |
| 3  | .sch.id     | 261613            |
| 4  | .my.id      | 255054            |
| 5  | .ac.id      | 211097            |
| 6  | .net.id     | 162538            |
| 7  | .go.id      | 157951            |
| 8  | .web.id     | 111324            |
| 9  | .or.id      | 65497             |
| 10 | .desa.id    | 30332             |
| 11 | .biz.id     | 10370             |
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