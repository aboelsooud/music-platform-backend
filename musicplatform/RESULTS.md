# Task #1

## Outline

* [import models](#import-models)
* [create some artists](#create-some-artists)
* [list down all artists](#list-down-all-artists)
* [list down all artists sorted by name](#list-down-all-artists-sorted-by-name)
* [list down all artists whose name starts with `a`](#list-down-all-artists-whose-name-starts-with-a)
* [create some albums and assign them to any artists](#create-some-albums-and-assign-them-to-any-artists) 
* [get the latest released album](#get-the-latest-released-album)
* [get all albums released before today](#get-all-albums-released-before-today)
* [get all albums released today or before but not after today](#get-all-albums-released-today-or-before-but-not-after-today)
* [count the total number of albums](#count-the-total-number-of-albums)
* [for each artist, list down all of his/her albums](#for-each-artist-list-down-all-of-his-or-her-albums) 
* [list down all albums ordered by cost then by name](#list-down-all-albums-ordered-by-cost-then-by-name)

### import models

```python
# import models and some datetime libraries
from artists.models import Artist
from albums.models import Album
from django.utils import timezone
from datetime import datetime
import pytz
```

### create some artists

```python
#creating artists
artist_1 = Artist(stage_name = "Kendrick Lamar", social_link = "https://www.instagram.com/kendricklamar/")
artist_1.save()

artist_2 = Artist(stage_name = "Steve Lacy", social_link = "https://www.instagram.com/steve.lacy/")
artist_2.save()

artist_3 = Artist(stage_name = "Frank Ocean", social_link = "https://www.instagram.com/blonded/")
artist_3.save()

artist_4 = Artist(stage_name = "A$AP Rocky", social_link = "https://www.instagram.com/asaprocky/")
artist_4.save()

artist_5 = Artist(stage_name = "SZA", social_link = "https://www.instagram.com/sza/")
artist_5.save()

artist_6 = Artist(stage_name = "Tyler, The Creator", social_link = "https://www.instagram.com/feliciathegoat/")
artist_6.save()
```

### list down all artists

```python
#print all objects using object manager
Artist.objects.all()

<QuerySet [<Artist: A$AP Rocky>, <Artist: Frank Ocean>, <Artist: Kendrick Lamar>, <Artist: SZA>, <Artist: Steve Lacy>, <Artist: Tyler, The Creator>]>
```

### list down all artists sorted by name

```python
#print orderd list of artists
Artist.objects.order_by('stage_name')

<QuerySet [<Artist: A$AP Rocky>, <Artist: Frank Ocean>, <Artist: Kendrick Lamar>, <Artist: SZA>, <Artist: Steve Lacy>, <Artist: Tyler, The Creator>]>
```

### list down all artists whose name starts with `a`

```python
#print artists whose names start with a or A
Artist.objects.filter(stage_name__startswith='a')

<QuerySet [<Artist: A$AP Rocky>]>
```

### create some albums and assign them to any artists

```python
#create albums in 2 different ways
album_1 = Album(artist = artist_1, name = "Mr. Morale & the Big Steppers", creation_date = datetime(2022, 1, 1, 12, 34, 56, tzinfo = pytz.utc), release_date = datetime(2022, 5, 13, 0, 0, 0, tzinfo = pytz.utc), cost = 199.99)
album_1.save()

album_2 = Album(artist = artist_2, name = "Gemini Rights", creation_date = datetime(2021, 12, 10, 0, 34, 56, tzinfo = pytz.utc), release_date = datetime(2022, 7, 15, 0, 0, 0, tzinfo = pytz.utc), cost = 52)
album_2.save()

album_3 = Album(artist = artist_3, creation_date = datetime(2019, 1, 30, 0, 0, 0, tzinfo = pytz.utc), release_date = datetime(2023, 1, 1, 0, 0, 0, tzinfo = pytz.utc), cost = 999.99)
album_3.save()

artist_4.album_set.create(creation_date = datetime(2021, 10, 10, 16, 1, 40, tzinfo = pytz.utc), release_date = datetime(2023, 6, 6, 6, 6, 6, tzinfo = pytz.utc), cost = 66.66)
<Album: New Album>

artist_5.album_set.create(name = "ctrl", creation_date = datetime(2016, 12, 12, 12, 12, 12, tzinfo = pytz.utc), release_date = datetime(2017, 6, 9, 0, 0, 0, tzinfo = pytz.utc), cost = 9.99)
<Album: ctrl>

album_6 = Album(artist = artist_6, name = "IGOR", creation_date = datetime(2015, 10, 9, 0, 34, 12, tzinfo = pytz.utc), release_date = datetime(2019, 5, 17, 0, 0, 0, tzinfo = pytz.utc), cost = 79.55)
album_6.save()

artist_6.album_set.create(name = "Call Me If You Get Lost", creation_date = datetime(2019, 6, 7, 0, 0, 0, tzinfo = pytz.utc), release_date = datetime(2021, 6, 25, 0, 0, 0, tzinfo = pytz.utc), cost = 89.99)
<Album: Call Me If You Get Lost>
```

### get the latest released album

```python
#get latest realesed album
Album.objects.latest('release_date')

<Album: New Album>
```

### get all albums released before today

```python
#get albums released before today
Album.objects.filter(release_date__date__lt = datetime.today())

<QuerySet [<Album: Mr. Morale & the Big Steppers>, <Album: Gemini Rights>, <Album: ctrl>, <Album: IGOR>, <Album: Call Me If You Get Lost>]>
```

### get all albums released today or before but not after today

```python
#get albums released today or before
Album.objects.filter(release_date__date__lte = datetime.today())

<QuerySet [<Album: Mr. Morale & the Big Steppers>, <Album: Gemini Rights>, <Album: ctrl>, <Album: IGOR>, <Album: Call Me If You Get Lost>]>
```

### count the total number of albums

```python
#get total number of albums
Album.objects.all().count()

7
```

### for each artist list down all of his or her albums

#### First way
```python
#get each artist albums
for artist in Artist.objects.all():
    artist.album_set.all()
 
<QuerySet [<Album: New Album>]>
<QuerySet [<Album: New Album>]>
<QuerySet [<Album: Mr. Morale & the Big Steppers>]>
<QuerySet [<Album: ctrl>]>
<QuerySet [<Album: Gemini Rights>]>
<QuerySet [<Album: IGOR>, <Album: Call Me If You Get Lost>]>
```

```python
for artist in Artist.objects.all():
    artist.stage_name
    artist.album_set.all()

'A$AP Rocky'
<QuerySet [<Album: New Album>]>
'Frank Ocean'
<QuerySet [<Album: New Album>]>
'Kendrick Lamar'
<QuerySet [<Album: Mr. Morale & the Big Steppers>]>
'SZA'
<QuerySet [<Album: ctrl>]>
'Steve Lacy'
<QuerySet [<Album: Gemini Rights>]>
'Tyler, The Creator'
<QuerySet [<Album: IGOR>, <Album: Call Me If You Get Lost>]>
```

#### Second way

```python
#get each artist albums
for artist in Artist.objects.all():
    Album.objects.filter(artist = artist)
 
<QuerySet [<Album: New Album>]>
<QuerySet [<Album: New Album>]>
<QuerySet [<Album: Mr. Morale & the Big Steppers>]>
<QuerySet [<Album: ctrl>]>
<QuerySet [<Album: Gemini Rights>]>
<QuerySet [<Album: IGOR>, <Album: Call Me If You Get Lost>]>
```

### list down all albums ordered by cost then by name

```python
#list albums ordered by cost then name
Album.objects.order_by('cost', 'name')

<QuerySet [<Album: ctrl>, <Album: Gemini Rights>, <Album: New Album>, <Album: IGOR>, <Album: Call Me If You Get Lost>, <Album: Mr. Morale & the Big Steppers>, <Album: New Album>]>
```

```python
for album in Album.objects.order_by('cost', 'name'):
    album.name
    album.cost
 
'ctrl'
Decimal('9.99')
'Gemini Rights'
Decimal('52.00')
'New Album'
Decimal('66.66')
'IGOR'
Decimal('79.55')
'Call Me If You Get Lost'
Decimal('89.99')
'Mr. Morale & the Big Steppers'
Decimal('199.99')
'New Album'
Decimal('999.99')
```
