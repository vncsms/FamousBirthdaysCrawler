# FamousBirthdaysCrawler

Crawler to get all birthdays from the site: https://www.famousbirthdays.com/

## Requirements:
`python 3.+` and `virtualenv`

## Install:
`pip3 install beautifulsoup4`

`pip install requests`

`pip install git+https://github.com/vncsms/FamousBirthdaysCrawler.git`

## How to use:

```python
import famous
birthdays = famous.get_all_people_birthday_day('june', 1)
#or if you want of the all year
birthdays = famous.get_all_people_birthday()
#or if you want by month
birthdays = famous.get_all_people_month('june')
```

## Output example:

```
[{
    "avatar": "https://www.famousbirthdays.com/faces/holland-tom-image.jpg",
    "birth_day": 1,
    "birth_month": 6,
    "body": "<div class=\"bio col-sm-7 col-md-8 col-lg-6\">\n<h2>About<a class=\"btn btn-default btn-sm btn-edit\" data-url=\"tom-holland.html\" href=\"#\" id=\"btn-edit\" title=\"Send Suggestion\"><i class=\"icn icn-edit\"></i></a></h2>\n<p>Best known for playing Spider-Man in the Marvel Cinematic Universe, including his debut starring role as the superhero in the 2017 film\u00a0<a href=\"https://www.famousbirthdays.com/movies/spider-man-homecoming.html\">Spider-Man: Homecoming</a>. Earlier in his acting career, he portrayed the title character in Billy Elliot: The Musical in London and starred in the 2012 feature\u00a0<a href=\"https://www.famousbirthdays.com/movies/the-impossible.html\">The Impossible</a>.\u00a0</p>\n<h2>Before Fame</h2>\n<p>He attended Donhead Preparatory School before being accepted by the BRIT School for Performing Arts and Technology. He later appeared in the UK version of\u00a0<a href=\"https://www.famousbirthdays.com/movies/thesecretworldofarrietty.html\">The Secret World of Arrietty</a>.</p>\n<h2>Trivia</h2>\n<p>He first appears as Spider-Man in the 2016 Marvel film\u00a0<a href=\"https://www.famousbirthdays.com/movies/civil-war.html\">Captain America: Civil War</a>.\u00a0</p>\n<h2>Family Life</h2>\n<p>His mother Nicola has worked as a photographer and his father, <a href=\"https://www.famousbirthdays.com/people/dominic-holland.html\">Dominic</a>, has worked as an author and a comedian. He has a pair of younger twin brothers named <a href=\"https://www.famousbirthdays.com/people/harry-holland.html\">Harry</a> and <a href=\"https://www.famousbirthdays.com/people/sam-holland.html\">Sam</a>. He also has another younger brother named\u00a0<a href=\"https://www.famousbirthdays.com/people/patrick-holland.html\">Patrick</a>.\u00a0</p>\n<h2>Associated With</h2>\n<p>He co-starred with\u00a0<a href=\"https://www.famousbirthdays.com/people/zendaya-coleman.html\">Zendaya</a>,\u00a0<a href=\"https://www.famousbirthdays.com/people/michael-keaton.html\">Michael Keaton</a>\u00a0and\u00a0<a href=\"https://www.famousbirthdays.com/people/jon-favreau.html\">Jon Favreau</a>\u00a0in\u00a0Spider-Man: Homecoming.\u00a0</p>\n</div>",
    "profession": "Movie Actor",
    "title": "Tom Holland",
    "year": 1996
},....]

```
