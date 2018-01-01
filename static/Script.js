


var images=['https://cdn.theatlantic.com/assets/media/img/mt/2016/04/RTX1GZCO/lead_960.jpg?1461074059',
'https://timedotcom.files.wordpress.com/2017/08/donald-trump-charlottesville-press-conference.jpg',
'https://thenypost.files.wordpress.com/2016/04/trumpchad.jpg?quality=90&strip=all',
'https://i.ytimg.com/vi/cg1QmrCt-XA/maxresdefault.jpg',
'http://cdn.newsapi.com.au/image/v1/b5d9ac7ac8b58a29f8320bb06aa07b2c']

document.body.style.backgroundImage = 'url('+images[3]+')';

var url=0;
setInterval(function(){
   url+=1;
  if(url==4){
    url=0;
  }
  document.body.style.backgroundImage = 'url('+images[url]+')';
  document.body.style.backgroundRepeat = "no-repeat";
  document.body.style.backgroundSize = "1250px 800px";


},5000);
