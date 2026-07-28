Pembaharuan terakhir: 28/07/26


# Kumpulan Dataset Domain Indonesia
Repository ini merupakan kumpulan domain atau situs website dengan TLD maupun ccTLD di Indonesia.

# Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation
Metodologi: https://tranco-list.eu/methodology
List ID: 46ZYX (2026-07-27)
lines: 17752
```
$ curl -O -J -L https://tranco-list.eu/download/46ZYX/full
$ tr -d '\r' < tranco_46ZYX_full.csv | awk -F',' '{print $2}' | grep '\.id$' > domains.txt

```

| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id (pure)  | 7352              |
| 2  | .co.id      | 3613              |
| 3  | .ac.id      | 1820              |
| 4  | .my.id      | 1175              |
| 5  | .go.id      | 869               |
| 6  | .sch.id     | 830               |
| 7  | .web.id     | 742               |
| 8  | .biz.id     | 524               |
| 9  | .net.id     | 488               |
| 10 | .or.id      | 288               |
| 11 | .mil.id     | 15                |
| 12 | .desa.id    | 32                |
| 13 | .ponpes.id  | 4                 |
|   Total |        | 17752             |

# ipsniper
| No | Domain | Jumlah |
|----|-------------|-------------------|
| 1  | .id         | 1437060           |
| 2  | .my.id      | 1087449           |
| 3  | .co.id      | 487379            |
| 4  | .web.id     | 379822            |
| 5  | .biz.id     | 325110            |
| 6  | .sch.id     | 219076            |
| 7  | .or.id      | 73578             |
| 8  | .desa.id    | 62458             |
| 9  | .ac.id      | 49829             |
| 10 | .go.id      | 13760             |
| 11 | .ponpes.id  | 5834              |
| 12 | .net.id     | 4978              |
| 13 | .mil.id     | 481               |
| 14 | .xn--9tfky.id | 41               |
| 15 | .kop.id     | 29                |
|  Total  |        | 4146884           |


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
| 1  | .id (pure)  | 634337            |
| 2  | .co.id      | 639898            |
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

# Cara mendapatkan data
Bagian ini menjelaskan langkah-langkah untuk mendapatkan atau memperbarui setiap dataset pada repositori ini.

## Tranco
Unduh list harian dari https://tranco-list.eu/latest_list, ambil kolom domain, lalu saring yang berakhiran `.id`. List ID berubah setiap hari — ganti `46ZYX` dengan ID terbaru.
```
$ curl -O -J -L https://tranco-list.eu/download/46ZYX/full
$ tr -d '\r' < tranco_46ZYX_full.csv | awk -F',' '{print $2}' | grep '\.id$' > Tranco/domains.txt
```
Untuk subset top-1M (domain dengan peringkat ≤ 1.000.000):
```
$ tr -d '\r' < tranco_46ZYX_full.csv | awk -F',' '$1<=1000000 && $2 ~ /\.id$/' | awk -F',' '{print $2}' | sort -u > Tranco/top-1m/domain.txt
```

## ipsniper
Unduh zonefile per TLD dari arsip publik ipsniper, lalu dekompresi.
```
$ mkdir -p ipsniper
$ for tld in ac biz co desa go kop mil my net or ponpes sch web xn--9tfky; do
>   curl -sL -o "ipsniper/$tld.id.txt.gz" \
>     "https://ipsniper.info/archive/latest/zonefiles/public/$tld.id.txt.gz"
> done
$ curl -sL -o ipsniper/id.txt.gz \
>   "https://ipsniper.info/archive/latest/zonefiles/public/id.txt.gz"
$ for f in ipsniper/*.gz; do gunzip -k "$f"; done
```
File `ipsniper/<tld>.id.txt` berformat zonefile: `domain\tIN\t<record>\t<value>` (A/AAAA/NS/CNAME).

## Domains Project
Sumber tidak menyediakan unduhan langsung per TLD; data .id tersedia sebagai satu shard `.xz` di mirror GitHub.
```
$ curl -sL -o "Domains Project/domain2multi-id00.txt.xz" \
>   "https://media.githubusercontent.com/media/tb0hdan/domains/master/data/indonesia/domain2multi-id00.txt.xz"
$ xz -dk "Domains Project/domain2multi-id00.txt.xz"
```
Untuk daftar lengkap TLD atau data negara lain: https://github.com/tb0hdan/domains (mirror `git lfs` + `./unpack.sh`). Versi raw di `https://dataset.domainsproject.org/` butuh autentikasi.

## Pembaharuan
Pembaharuan mengikuti siklus rilis sumber:
- **Tranco** — harian (https://tranco-list.eu/latest_list)
- **ipsniper** — bulanan, biasanya awal bulan (https://ipsniper.info/)
- **Domains Project** — tidak terjadwal, beberapa bulan sekali