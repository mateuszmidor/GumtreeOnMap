'''
Created on 02-08-2014
 
@author: mateusz
'''
 
import unittest
import setupdependencyinjectiontest  # @UnusedImport configures dependency injection for tests
from gumtreeoffers import GumtreeOffers
from injectdependency import InjectDependency
 
# this guy is used by GumtreeOffers.askForOffers   
class FakeQuerry():
    city = "defaultCity"
    def __str__(self):
        return "www.gumtree.pl/offers" # related to OffesFetcher first url in list
   
# this guy is used by GumtreeOffers.askForOffers
class GeocoderStub():
    @staticmethod
    def getCoordinates(address):
        return [10.01, 50.01]
         
# this guy is used by GumtreeOffers.askForOffers
class OffesFetcher():
    @staticmethod
    def fetchDocument(url):
        documents = {"www.gumtree.pl/offers&Page=1" : OFFERS_HTML,
                     "www.gumtree.pl/offer1" : OFFER1_HTML,
                     "www.gumtree.pl/offer2" : OFFER2_HTML}
        return documents[url]
    
# this guy is used by GumtreeOffers.askForOffers
class AddressResolverStub(): 
    @staticmethod
    def forCity(city):
        return AddressResolverStub()
    
    def resolve(self, *sources):
        return "Krakow, Poland"

class Test(unittest.TestCase):
    def setUp(self):
        InjectDependency.setDependency('urlfetcher', OffesFetcher)
        InjectDependency.setDependency('geocoder', GeocoderStub)       
        InjectDependency.setDependency('addressresolver', AddressResolverStub)       
 
    def testGetOffers(self):
        UNLIMITED_COUNT = 999
        offers = GumtreeOffers.askForOffers(FakeQuerry(), UNLIMITED_COUNT)
        self.assertEquals(2, len(offers))
        for offer in offers:
            self.assertTrue("address" in offer)
            self.assertTrue("longlatt" in offer)
            self.assertEquals([10.01, 50.01], offer["longlatt"]) # coords from GeocoderStub            
        
    def testGetOffersLimitedToOne(self):
        offers = GumtreeOffers.askForOffers(FakeQuerry(), 1)
        self.assertEquals(1, len(offers))
        for offer in offers:
            self.assertTrue("address" in offer)
            self.assertTrue("longlatt" in offer)
            self.assertEquals([10.01, 50.01], offer["longlatt"]) # coords from GeocoderStub  
         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

# html with 2 prepared offer urls
OFFERS_HTML = u"""
<!DOCTYPE html PUBLIC "-//W3C//DTD PAGE_WITH_OFFER_URLS 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Kraków Mieszkania, domy, pokoje, działki - sprzedaż i wynajem</title>
<meta http-equiv="X-UA-Compatible" content="IE=9"/>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<meta name="description" content="Znajdź ogłoszenia dla mieszkania i domy do wynajęcia"/>
<meta name="keywords" content="Gumtree, znajdź, ogłoszenia, mieszkania i domy do wynajęcia"/>
<meta name="uniq_GUMTREE_POLAND_page_token_name" content="SearchAd"/>
<meta name="robots" content="INDEX,FOLLOW"/>
<link rel="canonical" href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208"/>
<link rel="SHORTCUT ICON" href="http://pic.classistatic.com/image/pics/classifieds/gumtreeFavicon.ico">
<link href="http://www.gumtree.pl/f-SearchAdRss?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&CatId=9008&Keyword=ruczaj&Location=3200208&maxPrice=1600&maxPriceBackend=160000" rel="alternate" type="application/rss+xml" title="RSS">
<link rel="next" href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&Page=2">
<link href="http://include.classistatic.com/include/e884/c3css/pages/SearchAd-min.css" rel="stylesheet" type="text/css">
<link href="http://include.classistatic.com/include/e884/c3css/brands/gumtree/PL/all-pl.css" rel="stylesheet" type="text/css">
<script type="text/javascript">
//<!--
var picsPath = "http://pic.classistatic.com/image/pics/classifieds/";
var staticPath = "http://include.classistatic.com/include/e884/c3js/classifieds/rel1/";
var debugNonProdStaticPathPrefix = "s_isProduction => true, s_localStaticPath => null, m_isSecure => false, s_localSecureStaticPath => null, nonProdStaticPathPrefix => ";
//-->
</script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/shared_pages/adsense-min.js"></script>
<noscript>
<style type="text/css">
.jsonly {display:none;}
.collapseWithJS {display:block;}
.collapseWithJS_inline {display:inline;}
</style>
</noscript>
<script>
var kj_ads_queryParam = {"adsenseQuery":"ruczaj Kraków Małopolskie Nieruchomości mieszkania i domy do wynajęcia","afsChannels":"r_Krakow,Total,c_housing,l_l2,","locale":"pl-PL","adsenseClientAFS":"gumtree-pl","numGoogleTopAd":6,"isShowSitelink":false,"isLongerHeadlines":false,"type":"google","afcChannels":"r_Krakow,Total,c_housing,l_l2","pageNum":"1","totalAds":12,"isGoogleTest":false,"adSafe":false,"adsenseClientAFC":"ca-gumtree-pl_js","numGoogleAdRep":1,"invocationType":"afs"};
var kj_ads_dispParam = {"mediaplexDomain":"http://mktg.gumtree.pl/cm/bk/","toplayOut":"StyleF","topAdCount":6,"middleAdCount":1,"bottomStartIdx":7,"middlelayOut":"StyleF","mplxUrl":"9860-56167-3840-27?LocClass-AdSenseClick=1&amp;mpuid=;;;;;;;r_Krakow,c_housing;;1406754659614","bottomlayOut":"StyleF","middleStartIdx":6,"isSgNoImgVariantEnabled":false,"dispType":"srpMulti","trackType":"mplx","fixAdsenseImgAlignment":true};
kj_ads_dispParam.adSenseTitle = 'Linki sponsorowane';
kj_ads_dispParam.imgPlaceHolderIconUrl = 'http://pic.classistatic.com/image/pics/classifieds/en-IE/image_placeholder_large.gif';
</script>
<script>
Kj_ad.init(kj_ads_queryParam,kj_ads_dispParam);
</script>
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['siteTracker._setAccount', 'UA-9157637-1']);
_gaq.push(['siteTracker._setDomainName', '.gumtree.pl']);
_gaq.push(['siteTracker._setSessionCookieTimeout', 1800000]);
_gaq.push(['siteTracker._setCampaignCookieTimeout', 15768000000]);
_gaq.push(['siteTracker._setVisitorCookieTimeout', 63072000000]);
_gaq.push(['siteTracker._trackPageview', '/search/properties/flat+%2f+house+for+rent/attribute?query=ruczaj&category=properties^flat+%2f+house+for+rent^attribute']);
</script>
<script type="text/javascript">
(function() {
var ga = document.createElement("script");
ga.type = "text/javascript"; ga.async = true;
ga.src = ("https:" == document.location.protocol ? "https://ssl" : "http://www") + ".google-analytics.com/ga.js";
var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<script type="text/javascript">
var mpx_custom = {
new_mpcl: 's;krakow;9008;Nieruchomo%C5%9Bci;l3;;;;;;;http%3A%2F%2Fwww.gumtree.pl%2Ffp-mieszkania-i-domy-do-wynajecia%2Fkrakow%2Fruczaj%2Fc9008l3200208%3FA_ForRentBy%3Downr%26A_NumberRooms%3D2%26AdType%3D2%26maxPrice%3D1600%26maxPriceBackend%3D120000',
new_mpvl: document.referrer
}
</script>
</head>
<body>
<div id="main">
<div id="top">
<!-- google_ad_section_start(weight=ignore) -->
<div id="mediaplex_tracking"></div>
<script type="text/javascript">
(function() {
var mpxtag = document.createElement('script'); mpxtag.type = 'text/javascript'; mpxtag.async = true;
mpxtag.src = ('https:' == document.location.protocol
? 'https://secure.img-cdn.mediaplex.com/0/9860/56583/Kijiji-Poland_mp_pvt_brand_landing_ns_2013-04-30.js'
: 'http://img-cdn.mediaplex.com/0/9860/56583/Kijiji-Poland_mp_pvt_brand_landing_ns_2013-04-30.js');
var smpx = document.getElementsByTagName('script')[0]; smpx.parentNode.insertBefore(mpxtag, smpx);
})();
</script>
<!-- Start of HtmlPageHeader_03. This ftl is used for national site for Team 9 team -->
<script> var IsNC2_On = true; </script>
<script> var IsAdIdsSite_On = false; </script>
<table class="tbleColpse newHeader nationalSite">
<tr>
<td class="national-logo-area">
<div>
<a href="http://www.gumtree.pl" >
<img src="http://pic.classistatic.com/image/pics/classifieds/pl-PL/logo-gumtree.png" width="68" height="76" border="0" alt="Polska ">
</a>
</div> </td>
<td class="header-curve">
<div class="header-curve-top">&nbsp;</div>
<div class="header-curve-bottom">&nbsp;</div>
</td>
<td class="header-curve-space">
<div class="header-top-bg">&nbsp;</div>
<div class="header-bottom-bg">&nbsp;</div>
</td>
<td class="v-top">
<table width="100%" class="tbleColpse">
<tr>
<td class="navTabs-new h-top">
<div class="mainTabs">
<a href="http://www.gumtree.pl/c-SelectCategory" class="tabLink" >
<div id="SelectCategoryTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div> + Dodaj ogłoszenie</div>
</div></div></div>
</a>
<a href="http://www.gumtree.pl" class="tabLink" >
<div id="SiteHomeTab" class="tab activetab"><div class="tab-right"><div class="tab-mid"> <div id="SiteHomeText">Kategorie</div>
</div></div></div>
</a>
<a href="http://www.gumtree.pl/c-DealerDirectory" class="tabLink" >
<div id="DealerDirectoryTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div>Katalog sprzedawców</div>
</div></div></div>
</a>
</div>
</td>
<td class="lang h-top">
<div class="menuTop">
<ul>
<div id="withoutGreetings">
<li>
<!--<a href="https://secure.gumtree.pl/s-SignIn?rup=DefaultPage&ruq=A_ForRentBy%3Downr%26A_NumberRooms%3D2%26AdType%3D2%26CatId%3D9008%26Keyword%3Druczaj%26Location%3D3200208%26maxPrice%3D1600%26maxPriceBackend%3D120000" id="log_out" >here:Zaloguj się</a>-->
<span onclick="clickEncoded('aHR0cHM6Ly9zZWN1cmUuZ3VtdHJlZS5wbC9zLVNpZ25Jbj9ydXA9RGVmYXVsdFBhZ2UmcnVxPUFfRm9yUmVudEJ5JTNEb3duciUyNkFfTnVtYmVyUm9vbXMlM0QyJTI2QWRUeXBlJTNEMiUyNkNhdElkJTNEOTAwOCUyNktleXdvcmQlM0RydWN6YWolMjZMb2NhdGlvbiUzRDMyMDAyMDglMjZtYXhQcmljZSUzRDE2MDAlMjZtYXhQcmljZUJhY2tlbmQlM0QxMjAwMDA=')" class="sd-link">Zaloguj się</span>
<span class="bar">&nbsp;|&nbsp;</span>
</li>
<li>
<!--<a href="https://secure.gumtree.pl/s-StartRegistration?rup=DefaultPage&ruq=A_ForRentBy%3Downr%26A_NumberRooms%3D2%26AdType%3D2%26CatId%3D9008%26Keyword%3Druczaj%26Location%3D3200208%26maxPrice%3D1600%26maxPriceBackend%3D120000" id="log_out" >here:Zarejestruj się</a>-->
<span onclick="clickEncoded('aHR0cHM6Ly9zZWN1cmUuZ3VtdHJlZS5wbC9zLVN0YXJ0UmVnaXN0cmF0aW9uP3J1cD1EZWZhdWx0UGFnZSZydXE9QV9Gb3JSZW50QnklM0Rvd25yJTI2QV9OdW1iZXJSb29tcyUzRDIlMjZBZFR5cGUlM0QyJTI2Q2F0SWQlM0Q5MDA4JTI2S2V5d29yZCUzRHJ1Y3phaiUyNkxvY2F0aW9uJTNEMzIwMDIwOCUyNm1heFByaWNlJTNEMTYwMCUyNm1heFByaWNlQmFja2VuZCUzRDEyMDAwMA==')" class="sd-link">Zarejestruj się</span>
<span class="bar">&nbsp;|&nbsp;</span>
</li>
<li>
<!--<a href="http://www.gumtree.pl/c-ManageMyAds" id="log_out" >here:Moje Gumtree</a>-->
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtTWFuYWdlTXlBZHM=')" class="sd-link">Moje Gumtree</span>
</li>
</div>
</ul>
</div>
</td>
</tr>
</table>
<noscript>
<style>
.msgbar{
padding-top:5px;
}
</style>
</noscript>
<table class="search-area tbleColpse header-bottom-bg">
<tr>
<td style="padding-right:10px" nowrap="true" valign="middle">
<table class="tbleColpse rel-p" width="100%" >
<tr>
<td nowrap="true" align="left">
<table class="tbleColpse">
<form action="http://www.gumtree.pl/f-SearchAdRedirect" method="get" name="frmSearchAd" id="frmSearchAd" class="searchform">
<input type="hidden" name="isSearchForm" value="true">
<tr>
<td><div class="ww_table_left"></div></td>
<td align="left" >
<table class="tbleColpse" >
<!--
<tr>
<td class="ww_table">
<div class="toplbl">here:Czego szukasz...?</div>
</td>
</tr>
-->
<tr>
<td class="ww_table" style="padding-right:10px">
<div class="flt">
<span class="left-what"></span>
<span class="keySpan lf">
<input title="Czego szukasz...?" id="autoComp" type="text" name="Keyword" value="ruczaj" class="keyword center-what" autocomplete="off"/>
</span>
<span class="right-what"></span>
</div>
</td>
</tr>
</table>
</td>
<td class="ww_table" style="padding-right:10px">
<div id="searchCat" class="jsonly kjmenu_main_wrap">
<div class="left-all-cat"></div>
<div id="searchCat_name" class="center-all-cat">mieszkania i domy do wynajęcia<img border="0" src="http://pic.classistatic.com/image/pics/classifieds/spacer.gif" width="25px" height="1px"/></div>
<div class="button-arrow"></div>
</div>
<input class="jsonly" type="hidden" name="CatId" value="9008"/>
</td>
<td class="ww_table">
<div id="searchLoc" class="jsonly kjmenu_main_wrap">
<div class="left-all-cat"></div>
<div id="searchLoc_name" class="center-all-cat">Kraków<img border="0" src="http://pic.classistatic.com/image/pics/classifieds/spacer.gif" width="25px" height="1px"/></div>
<div class="button-arrow"></div>
</div>
<input class="jsonly" type="hidden" name="Location" value=""/>
</td>
<td class="ww_table" style="padding-left:10px">
<span class="left-search"></span>
<input id="searchAdGo" type="submit" value="Szukaj" class="searchButton" />
<span class="right-search"></span>
</td>
<td><div class="ww_table_right"></div></td>
</tr>
<input class="sfasp" type="hidden" name="maxPriceBackend" value="160000"/>
<input class="sfasp" type="hidden" name="maxPrice" value="1600"/>
<input class="sfasp" type="hidden" name="A_NumberRooms" value="2"/>
<input class="sfasp" type="hidden" name="AdType" value="2"/>
<input class="sfasp" type="hidden" name="A_ForRentBy" value="ownr"/>
</form>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<div id="CategoryDropdown" class="popupWindow">
<ul class="catlistdropdown">
<li class="item">
<span class="cursptr" id="catId0" onClick="swapCat(this,'0');">Wszystkie ogłoszenia</span>
</li>
<li class="item">
<span class="cursptr" id="catId9000" onClick="swapCat(this,'9000');">pokoje do wynajęcia</span>
</li>
<li class="item">
<span class="cursptr" id="catId9008" onClick="swapCat(this,'9008');">mieszkania i domy do wynajęcia</span>
</li>
<li class="item">
<span class="cursptr" id="catId9073" onClick="swapCat(this,'9073');">mieszkania i domy - sprzedam i kupię</span>
</li>
<li class="item">
<span class="cursptr" id="catId9194" onClick="swapCat(this,'9194');">działki</span>
</li>
<li class="item">
<span class="cursptr" id="catId9074" onClick="swapCat(this,'9074');">krótki termin i noclegi</span>
</li>
<li class="item">
<span class="cursptr" id="catId9193" onClick="swapCat(this,'9193');">kwatery i domki letniskowe</span>
</li>
<li class="item">
<span class="cursptr" id="catId9072" onClick="swapCat(this,'9072');">lokal i biuro</span>
</li>
<li class="item">
<span class="cursptr" id="catId9071" onClick="swapCat(this,'9071');">parking i garaż</span>
</li>
</ul>
</div>
<div class=popWords>
<div class="floatLeft30px">
Powiązane
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+pok%C3%B3j/c9008l3200208" title="ruczaj pokój">ruczaj pokój</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+mieszkania/c9008l3200208" title="ruczaj mieszkania">ruczaj mieszkania</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/kawalerka+ruczaj/c9008l3200208" title="kawalerka ruczaj">kawalerka ruczaj</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+obozowa/c9008l3200208" title="ruczaj obozowa">ruczaj obozowa</a>
</div>
</div>
<div class="greyBottom300">
</div>
<div id="pagestatus_new" style="">
</div>
<!-- google_ad_section_end(weight=ignore) -->
</div>
<div id="middle" class="page_searchad">
<div id="breadcrumbSB">
<div itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>
<!-- google_ad_section_start -->
<td height="25" width="43%" nowrap align="left">&nbsp;
<a href="http://www.gumtree.pl/fp-malopolskie/l3200003" itemprop="url">
<span itemprop="title">Małopolskie</span>
</a>
>
<a href="http://www.gumtree.pl/fp-krakow/l3200208" itemprop="url">
<span itemprop="title">Kraków</span>
</a>
&gt; <a href="http://www.gumtree.pl/fp-nieruchomosci/krakow/ruczaj/c2l3200208?AdType=2&maxPrice=1600&maxPriceBackend=160000" itemprop="url">
<span itemprop="title">Nieruchomości</span>
</a>
>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000" itemprop="url">
<span itemprop="title">mieszkania i domy do wynajęcia</span>
</a>
&gt; <span itemprop="title" style="font-weight:bold;"><h1>Kraków Mieszkania domy do wynajęcia</h1></span>
</td>
<td height="25" width="54%" align="right">
</td>
<td height="25" width="1%" align="right">
&nbsp;
</td>
<!-- google_ad_section_end -->
</tr>
</table>
</div>
</div>
<div class="sbBucket">
<div id='div-gpt-ad-topbanner' style='text-align:center;margin:0px auto'></div></div>
<div class="sbBucket">Poniżej znajdują się wyniki wyszukiwania dla "<b>ruczaj</b>" w kategorii: "dom / mieszkanie do wynajęcia" na Gumtree Polska.<br />
Kliknij na jeden z poniższych ogłoszeń w dziale Polska dom/mieszkanie do wynajęcia, by poznać więcej szczegółów.
</div>
<!-- Category h1 -->
<table class="tblClpsePad clr" width="100%">
<tr>
<td class="srchlft" >
<div id="sbLeftNav" class="styleA">
<div class="innerLeftNav" style="padding-left:10px">
<div id="search-nav2">
<span class="listtitle" id="refineResults">Obecne zestawienia <span class="titlecount">(92)</span></span>
<div>
<div class="filter">
<span class="filterTitle" id="categoryLabel">Kategoria:</span>
<div style="padding-left:10px;">
<a href="http://www.gumtree.pl/fp-ruczaj/krakow/l3200208?AdType=2&maxPrice=1600&maxPriceBackend=160000">Wszystkie kategorie</a>
</div>
</#--if-->
<div style="padding-left:20px;">
<a href="http://www.gumtree.pl/fp-nieruchomosci/krakow/ruczaj/c2l3200208?AdType=2&maxPrice=1600&maxPriceBackend=160000">Nieruchomości</a>
</div>
</#--if-->
<div class="selectedItem_x " style="padding-left:30px;">
<strong>mieszkania i domy do wynajęcia</strong>
&nbsp;(92)
<a href="http://www.gumtree.pl/fp-nieruchomosci/krakow/ruczaj/c2l3200208?AdType=2&maxPrice=1600&maxPriceBackend=160000" class="close_x"></a>
</div>
</#--if-->
</div>
<div class="separatedfilter filter">
<span class="filterTitle" id="locationFilter">Miejsce:</span><br/>
<div style="padding-left:10px;">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/ruczaj/c9008?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000">Polska</a>
</div>
</#--if-->
<div style="padding-left:20px;">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/malopolskie/ruczaj/c9008l3200003?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000">Małopolskie</a>
</div>
</#--if-->
<div class="selectedItem_x " style="padding-left:30px;">
<strong>Kraków</strong>
&nbsp;(92)
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/malopolskie/ruczaj/c9008l3200003?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000" class="close_x"></a>
</div>
</#--if-->
</div>
<div class="separatedfilter filter">
<span class="filterTitle" id="adTypeFilter">Rodzaj:</span><br/>
<div style="padding-left:10px;">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&maxPrice=1600&maxPriceBackend=160000">Wszystkie rodzaje</a>
</div>
</#--if-->
<div class="selectedItem_x " style="padding-left:20px;">
<strong>Oferuję</strong>
&nbsp;(92)
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&maxPrice=1600&maxPriceBackend=160000" class="close_x"></a>
</div>
</#--if-->
</div>
<div class="separatedfilter filter">
<span class="filterTitle" id="featuresFilter">Ogłoszenia wyróżnione:</span><br/>
<div class="selectedItem_x2 " style="padding-left:10px;">
<strong>Wszystkie ogłoszenia wyróżnione</strong>
</div>
</#--if-->
<div style="padding-left:20px;">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&urgentAd=true">Ogłoszenia pilne</a>
</div>
</#--if-->
</div>
</div>
<form id="priceFilterForm" name="priceFilterForm" class="separatedfilter filter goOnKeyup" action='http://www.gumtree.pl/f-SearchAd?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&CatId=9008&Keyword=ruczaj&Location=3200208&maxPriceBackend=120000'
method="POST" style="margin-bottom:5px;" >
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lbl" >Cena:</span>
</div>
<div class="first-input">
<input name="minPrice" class="minPriceInput" maxlength="12" type="text" title="od" value=""> - <input name="maxPrice" class="maxPriceInput" maxlength="12" type="text" title="do" value="1 600">
</div>
</div>
<input type="submit" class="newButton collapseWithJS" value="Idź">
</form>
<div class="separatedfilter filter">
<div class="filterTitle"><span class="ForRentBy">Do wynajęcia przez:</span></div>
<div style="padding-left:10px"><a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000">Jakikolwiek</a></div>
<div class="selectedItem_x" style="padding-left:10px">Właściciel<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000" class="close_x"></a></div>
</div>
<div class="jsonly moreOptions" style="padding:0px 0px 5px 10px"><a href="#" class="filterPopup"
id="ForRentByFilter">Zobacz więcej opcji...</a></div>
<div class="separatedfilter filter">
<div class="filterTitle"><span class="DwellingType">Rodzaj nieruchomości:</span></div>
<div style="padding-left:10px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_DwellingType=flat&A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000">Mieszkanie</a>
(91)
</div>
<div style="padding-left:10px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_DwellingType=other&A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000">Inne</a>
(1)
</div>
<div style="padding-left:10px">
Dom
(0)
</div>
</div>
<div class="separatedfilter filter">
<div class="filterTitle"><span class="NumberRooms">Liczba pokoi:</span></div>
<div style="padding-left:10px"><a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&AdType=2&maxPrice=1600&maxPriceBackend=160000">Jakikolwiek</a></div>
<div class="selectedItem_x" style="padding-left:10px">2 pokoje<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&AdType=2&maxPrice=1600&maxPriceBackend=160000" class="close_x"></a></div>
</div>
<div class="jsonly moreOptions" style="padding:0px 0px 5px 10px"><a href="#" class="filterPopup"
id="NumberRoomsFilter">Zobacz więcej opcji...</a></div>
<form class="separatedfilter filter goOnKeyup" action='http://www.gumtree.pl/f-SearchAd?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&CatId=9008&Keyword=ruczaj&Location=3200208&maxPrice=1600&maxPriceBackend=120000' method="POST" style="margin-bottom:5px;">
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblA_AreaInMeters" >Wielkość (m2):</span>
</div>
<div class="first-input">
<a name="A_AreaInMeters"></a>
<input type="text" style="width: 90px;" name="A_AreaInMeters_min" value="22" title="od"> - <input type="text" style="width: 90px;" name="A_AreaInMeters_max" value="44" title="do">
</div>
</div>
<input type="submit" class="newButton collapseWithJS" value="Idź">
</form>
</div>
<div class="listmodule extrakeywords">
<span class="listtitle">Powiązane wyszukiwania</span>
<ul class="clearfix">
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+kawalerka/c9008l3200208" title="ruczaj kawalerka">ruczaj kawalerka</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie+ruczaj/c9008l3200208" title="mieszkanie ruczaj">mieszkanie ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie+do+wynaj%C4%99cia+ruczaj/c9008l3200208" title="mieszkanie do wynajęcia ruczaj">mieszkanie do wynajęcia ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+chmieleniec/c9008l3200208" title="ruczaj chmieleniec">ruczaj chmieleniec</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/krakow+ruczaj/c9008l3200208" title="krakow ruczaj">krakow ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/krak%C3%B3w+ruczaj/c9008l3200208" title="kraków ruczaj">kraków ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/bobrzy%C5%84skiego+ruczaj/c9008l3200208" title="bobrzyńskiego ruczaj">bobrzyńskiego ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+z+ogr%C3%B3dkiem/c9008l3200208" title="ruczaj z ogródkiem">ruczaj z ogródkiem</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+torfowa/c9008l3200208" title="ruczaj torfowa">ruczaj torfowa</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+2+pokojowe/c9008l3200208" title="ruczaj 2 pokojowe">ruczaj 2 pokojowe</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+ul+pszczelna/c9008l3200208" title="ruczaj ul pszczelna">ruczaj ul pszczelna</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+ul+obozowa/c9008l3200208" title="ruczaj ul obozowa">ruczaj ul obozowa</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+czerwone+maki/c9008l3200208" title="ruczaj czerwone maki">ruczaj czerwone maki</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+raciborska/c9008l3200208" title="ruczaj raciborska">ruczaj raciborska</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/niezale%C5%BCne+ruczaj/c9008l3200208" title="niezależne ruczaj">niezależne ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/2+pokoje+ruczaj/c9008l3200208" title="2 pokoje ruczaj">2 pokoje ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+pszczelna/c9008l3200208" title="ruczaj pszczelna">ruczaj pszczelna</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+apartament/c9008l3200208" title="ruczaj apartament">ruczaj apartament</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+i/c9008l3200208" title="ruczaj i">ruczaj i</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+3/c9008l3200208" title="ruczaj 3">ruczaj 3</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+bobrzy%C5%84skiego/c9008l3200208" title="ruczaj bobrzyńskiego">ruczaj bobrzyńskiego</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+mieszkanie/c9008l3200208" title="ruczaj mieszkanie">ruczaj mieszkanie</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/2+pokoje+mieszkanie+ruczaj/c9008l3200208" title="2 pokoje mieszkanie ruczaj">2 pokoje mieszkanie ruczaj</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/bobrzy%C5%84skiego+or+chmieleniec+or+ruczaj+or+drukarska/c9008l3200208" title="bobrzyńskiego or chmieleniec or ruczaj or drukarska">bobrzyńskiego or chmieleniec or ruczaj or drukarska</a>
</li>
<li>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj+24/c9008l3200208" title="ruczaj 24">ruczaj 24</a>
</li>
</ul>
</div>
<div class="listmodule" id="subInvite" >
<div>
<span class="listtitle">
Powiadomienia na Gumtree
<span class="helptip">
<span class="sudo-link">[?]</span>
</span>
</span>
</div>
<div style="padding-left:5px;">
Otrzymuj codziennie e-mail z najnowszymi wynikami dla tego wyszukiwania
</div>
<div style="padding:5px">
<input id="subscribe" type="button" value="Zamów" class="newButton"/>
</div>
</div>
<div id="adlink"></div>
<div id='div-gpt-ad-leftskyscraper' style='width:160px;height:600px;margin:10px auto'></div>
<p></p>
<p></p>
</div>
</div>
<div id="filterPopup" class="dialog" style="width:600px">
<div class="dialogHeadingContainer">
<div class="dialogHeadingRight">
<div class="dialogHeading clearfix">
<div class="dialogTitle">Więcej filtrów</div>
<div class="dialogCloseBtn close" title="Zamknij">&nbsp;</div>
</div>
</div>
</div>
<div class="dialogContentContainer">
<div class="dialogContent" >
<table class="tbleColpse" width="99%"><tr>
<td class="navs" valign="top" nowrap style="padding-bottom:10px">
<div id="priceFilterTab">Cena</div>
<div id="ForRentByFilterTab">Do wynajęcia przez</div>
<div id="DwellingTypeFilterTab">Rodzaj nieruchomości</div>
<div id="NumberRoomsFilterTab">Liczba pokoi</div>
<div id="AreaInMetersFilterTab">Wielkość (m2)</div>
</td>
<td id="filterContent" class="fltrcell">
<div class="filterContent">
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lbl" >Wpisz zakres cen</span>
</div>
<div class="first-input">
<input name="minPrice" class="minPriceInput" maxlength="12" type="text" title="od" value=""> - <input name="maxPrice" class="maxPriceInput" maxlength="12" type="text" title="do" value="1 600">
</div>
</div>
</div>
<div class="filterContent">
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblA_ForRentBy" >Do wynajęcia przez:</span>
</div>
<div class="first-input">
<a name="A_ForRentBy"></a>
<div class="input-div">
<ul>
<li><input type="checkbox" name="A_ForRentBy" value="ownr" checked/> Właściciel</li>
<li><input type="checkbox" name="A_ForRentBy" value="agncy" /> Agencja</li>
</ul>
</div>
</div>
</div>
</div>
<div class="filterContent">
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblA_DwellingType" >Rodzaj nieruchomości:</span>
</div>
<div class="first-input">
<a name="A_DwellingType"></a>
<div class="input-div">
<ul>
<li><input type="checkbox" name="A_DwellingType" value="flat" /> Mieszkanie</li>
<li><input type="checkbox" name="A_DwellingType" value="house" /> Dom</li>
<li><input type="checkbox" name="A_DwellingType" value="other" /> Inne</li>
</ul>
</div>
</div>
</div>
</div>
<div class="filterContent">
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblA_NumberRooms" >Liczba pokoi:</span>
</div>
<div class="first-input">
<a name="A_NumberRooms"></a>
<div class="input-div">
<ul>
<li><input type="checkbox" name="A_NumberRooms" value="10" /> Kawalerka lub garsoniera</li>
<li><input type="checkbox" name="A_NumberRooms" value="2" checked/> 2 pokoje</li>
<li><input type="checkbox" name="A_NumberRooms" value="3" /> 3 pokoje</li>
<li><input type="checkbox" name="A_NumberRooms" value="4" /> 4 pokoje</li>
<li><input type="checkbox" name="A_NumberRooms" value="5" /> 5 pokoi</li>
<li><input type="checkbox" name="A_NumberRooms" value="6" /> 6 lub więcej pokoi</li>
</ul>
</div>
</div>
</div>
</div>
<div class="filterContent">
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblA_AreaInMeters" >Wielkość (m2):</span>
</div>
<div class="first-input">
<a name="A_AreaInMeters"></a>
<input type="text" style="width: 90px;" name="A_AreaInMeters_min" value="" title="od"> - <input type="text" style="width: 90px;" name="A_AreaInMeters_max" value="" title="do">
</div>
</div>
</div>
</td>
</tr></table>
<div class="actionBar">
<input id="updateSearch" type="submit" class="newButton" value="Aktualizuj"> <a href="#" class="close">Anuluj</a>
</div>
</div>
</div>
<div class="dialogFooterContainer">
<div class="dialogFooterRight">
<div class="dialogFooter"></div>
</div>
</div>
</div>
</td>
<td class="srchrht">
<div id="sbResultsListing">
<div class="sbInnerDiv">
<table id="SNB_Results" class="tblClpsePad" cellpadding="0" width="100%" ><col width='40px'/><col width='130px' /><col/><col width='10%'/><col width='13%'/>
<tr class="SNB_header">
<td class="snb_header_col_first" colspan="3" >
<table cellpadding=0 cellspacing=0 border=0 class="galleryMenuFill"><tr>
<td class="sbRHLeft">
<strong>Zobacz jako</strong>
<span class="listViewActive">&nbsp;</span>
Lista
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2ZwLW1pZXN6a2FuaWEtaS1kb215LWRvLXd5bmFqZWNpYS9rcmFrb3cvcnVjemFqL2M5MDA4bDMyMDAyMDg/QV9Gb3JSZW50Qnk9b3duciZBX051bWJlclJvb21zPTImQWRUeXBlPTImZ2FsbGVyeT10cnVlJm1heFByaWNlPTE2MDAmbWF4UHJpY2VCYWNrZW5kPTE2MDAwMA==')" class="galleryView">&nbsp;</span>
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2ZwLW1pZXN6a2FuaWEtaS1kb215LWRvLXd5bmFqZWNpYS9rcmFrb3cvcnVjemFqL2M5MDA4bDMyMDAyMDg/QV9Gb3JSZW50Qnk9b3duciZBX051bWJlclJvb21zPTImQWRUeXBlPTImZ2FsbGVyeT10cnVlJm1heFByaWNlPTE2MDAmbWF4UHJpY2VCYWNrZW5kPTE2MDAwMA==')" class="sudo-link">Galeria</span>
</td><td><div class="galleryMenuSeparator"></div></td>
</tr></table>
</td>
<td class="prc snb_header_col" >
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2ZwLW1pZXN6a2FuaWEtaS1kb215LWRvLXd5bmFqZWNpYS9rcmFrb3cvcnVjemFqL2M5MDA4bDMyMDAyMDg/QV9Gb3JSZW50Qnk9b3duciZBX051bWJlclJvb21zPTImQWRUeXBlPTImU29ydD0zJm1heFByaWNlPTE2MDAmbWF4UHJpY2VCYWNrZW5kPTE2MDAwMA==')" class="sudo-link ">Cena</span>
</td>
<td class="snb_header_col snb_header_col_last posted" >
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2ZwLW1pZXN6a2FuaWEtaS1kb215LWRvLXd5bmFqZWNpYS9rcmFrb3cvcnVjemFqL2M5MDA4bDMyMDAyMDg/QV9Gb3JSZW50Qnk9b3duciZBX051bWJlclJvb21zPTImQWRUeXBlPTImU29ydD0xJm1heFByaWNlPTE2MDAmbWF4UHJpY2VCYWNrZW5kPTE2MDAwMA==')" class="sudo-link sortDesc">
Dodane
</span>
</td>
</tr>
<tr>
<td colspan="5" >
</td>
</tr>
<tr>
<td colspan="5">
</td>
</tr>
<tr>
<td colspan="5"></td>
</tr>
<tr>
<td colspan="5" class="pad0">
<div id="topAdSense"></div>
<script>
Kj_ad.displayAdsense({id:"topAdSense",dispType:"srpTop"});
</script>
</td>
</tr>
<tr>
<td colspan="5" class="pad0">
<div class="sbTopadWrapper rmBtmBrdr">
<div class="sbTopadTitleRow clearfix">
<div class="sbTopadTitleText">
<b>
Ogłoszenia wyróżnione
</b>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&featuredAd=true&maxPrice=1600&maxPriceBackend=160000">Zobacz wszystkie</a>
</div>
<div>
<div class="sbTopadHelp">Chcesz tutaj wypromować swoje ogłoszenie? <a href="/p-FeaturedAdFAQ">Dowiedz się więcej</a></div>
</div>
</div>
</div>
</td>
</tr>
<!-- google_ad_section_start -->
<!--<td width=55 align=center valign=middle class="watch " >-->
<!--</td>-->
<tr class="resultsTableSB rrow" id="resultFeatRow0" valign="top">
<td class="ar-items clearfix" colspan="3" >
<div class="ar-image"> <div class="image-thumb">
<div class="image-cnt">
<img class="thumbnail thumbImg" src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/PEYAAOSwd4tT2Q9n/$_2.JPG" alt="Gumtree: Mieszkanie 2-pokoje, 45m2, wyposażone, szuwarowa" border="0" />
</div>
</div>
</div>
<div class="ar-text-wrap clearfix">
<div class="ar-title">
<a href="www.gumtree.pl/offer1"</a><br/>
</div>
<div class="ar-descr"> <span >Oferuję do wynajęcia ładne mieszkanie na Ruczaju przy ul. Pszczelnej. Mieszkanie zlokalizowane na 2 piętrze w bloku oddanym w 2009 roku. Pokoje nieprzechodnie (w każdym z pokoi dwuosobowa wersalka), kuchnia, łazienka. Mieszkanie w pełni wyposażone i urządzone. Mieszkanie znajduje się w otoczeniu zieleni w spokojnej okolicy. W bliskiej odległości przystanki komunikacji miejskiej (autobus i tramwaj) oraz sklepy. Zapraszamy do oglądnięcia mieszkania Koszt: 1500 zł odstępne + czynsz (150 zł) + media ...</span>
<div class="search_row_cat_name_wrapper">
<a class="search_row_cat_name search_row_cat_name-9008" href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/c9008">mieszkania i domy do wynajęcia</a>
</div>
</div>
<div>
</td>
<td class="ar-items">
<div class="ar-price">
<strong> Zł  1 500
</strong>
</div>
</td>
<td class="ar-items ar-right">
<div class="ar-wrap">
<div class="ar-container">
<div class="ar-date">
&nbsp;
</div>
<div class="ar-watch">
<div class="saveArea" style="display:inline">
<div class="607012750" style="display:block"></div>
</div>
</div>
</div>
</div>
</td>
</tr>
<!-- google_ad_section_end -->
<tr><td colspan="5" class="rsTop">
<div class="sbTopadWrapper btbrdr">&nbsp;</div>
</td></tr>
<!-- google_ad_section_start -->
<!--<td width=55 align=center valign=middle class="watch " >-->
<!--</td>-->
<tr class="resultsTableSB rrow" id="resultRow0" valign="top">
<td class="ar-items clearfix" colspan="3" >
<div class="ar-image"> <div class="image-thumb">
<div class="image-cnt">
<img class="thumbnail thumbImg" src="http://i.ebayimg.com/00/s/MjYzWDc5OQ==/z/qtwAAOSwq7JT2Usp/$_2.JPG" alt="Gumtree: MIESZKANIE NA RUCZAJU" border="0" />
</div>
</div>
</div>
<div class="ar-text-wrap clearfix">
<div class="ar-title">
<a href="www.gumtree.pl/offer2"</a><br/>
</div>
<div class="ar-descr"> <span >.....Do wynajęcia mieszkanie 2 pokojowe w dzielnicy <u>RUCZAJ</u> przy ul.RACIBORSKIEJ. Szybki dojazd do centrum, bardzo dobra komunikacja – tramwaje, autobusy. Doskonała infrastruktura osiedla – szkoły, przedszkola, basen, liczne markety. Mieszkanie ma 46 m2, mieści się na 3 piętrze w bloku. Mieszkanie składa się z dwóch oddzielnych pokoi, oddzielnej kuchni, korytarza, łazienki. Mieszkanie jest umeblowane. Mogą zamieszkać nawet 4 osoby, mile widziani studenci
Zapraszam do oglądania mieszkania.</span>
<div class="search_row_cat_name_wrapper">
<a class="search_row_cat_name search_row_cat_name-9008" href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/c9008">mieszkania i domy do wynajęcia</a>
</div>
</div>
<div>
</td>
<td class="ar-items">
<div class="ar-price">
<strong> Zł  1 450
</strong>
</div>
</td>
<td class="ar-items ar-right">
<div class="ar-wrap">
<div class="ar-container">
<div class="ar-date">
<ul>
<li> &lt; 1 godz. temu
</li>
</ul>
</div>
<div class="ar-watch">
<div class="saveArea" style="display:inline">
<div class="607942385" style="display:block"></div>
</div>
</div>
</div>
</div>
</td>
</tr>
<!--<td width=55 align=center valign=middle class="watch " >-->
<!--</td>-->
<tr class="resultsTableSB rrow" id="resultRow1" valign="top">
<td class="ar-items clearfix" colspan="3" >
<div class="ar-image"> <div class="image-thumb">
<div class="image-cnt">
<img class="thumbnail thumbImg" src="http://i.ebayimg.com/00/s/NjgwWDEwMjQ=/z/kYsAAOSwbqpT2Twg/$_2.JPG" alt="Gumtree: Wynajmę studentkom dwupokojowe mieszkanie 37m²" border="0" />
</div>
</div>
</div>
</div>
</td>
</tr>
<!--<td width=55 align=center valign=middle class="watch " >-->
<!--</td>-->
<tr class="resultsTableSB rrow" id="resultRow2" valign="top">
<td class="ar-items clearfix" colspan="3" >
<div class="ar-image"> <div class="image-thumb">
<div class="image-cnt">
<img class="thumbnail thumbImg" src="http://i.ebayimg.com/00/s/MjYzWDc5OQ==/z/HvEAAOSwPe1T2TP5/$_2.JPG" alt="Gumtree: MIESZKANIE NA RUCZAJU" border="0" />
</div>
</div>
</div>
 
<!-- google_ad_section_end -->
</table>
<!-- google_ad_section_end -->
<div id="bottomAdSense" style="clear:left"></div>
<script>
Kj_ad.displayAdsense({id:"bottomAdSense",dispType:"srpBottom"});
</script>
<table class="paginationBottomBg" width="100%" cellpadding=0 cellspacing=0 border=0>
<tr>
<td>
<div class="pageLabel">Strona: </div>
<div class="currentPage">1</div>
<div class="notCurrentPage">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&Page=2">2</a>
</div>
<div class="notCurrentPage">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&Page=3">3</a>
</div>
<div class="notCurrentPage">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&Page=4">4</a>
</div>
<div class="notCurrentPage">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&Page=5">5</a>
</div>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/ruczaj/c9008l3200208?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&maxPrice=1600&maxPriceBackend=160000&Page=2" class="prevNextLink">Nomorepagesnbsp;&gt;</a>
</td>
<td class="paginationBottomBg_right" align=right valign=middle> <a href="http://www.gumtree.pl/f-SearchAdRss?A_ForRentBy=ownr&A_NumberRooms=2&AdType=2&CatId=9008&Keyword=ruczaj&Location=3200208&maxPrice=1600&maxPriceBackend=160000"><img src="http://pic.classistatic.com/image/pics/classifieds/xml.gif" alt="RSS" border="0"></a>
</td>
</tr>
</table>
<div id='div-gpt-ad-bottombanner' style='width:728px;height:90px;margin:0px auto'></div>
</div>
</div>
</td>
</tr>
</table>
</div>
<div id="bottom">
<!-- google_ad_section_start(weight=ignore) -->
<div class="footer">
<div>
<link type="text/css" rel="stylesheet" href="https://securepic.classistatic.com/image/site/au/global_footer/new_global_footer.css" />
<style type="text/css">
.footer {
border-top: 0px solid #BEC3C7;
margin: 0px 0px 0px 15px;
padding: 10px 0 10px 0;
}
.footer li {
list-style:none;
display: list-item;
color: #676B5C;
font-size:11px;
margin:0;
padding:0 5px 0 0;
border-right: 0px solid #ffffcc;
}
.get-to-know-us,.explore-gumtree,.legalbits,.tips-help,.blog-latest,.gumtree-elsewhere{
display:inline;
float:left;
}
.get-to-know-us{
margin-left:10px;
}
.blog-latest{
margin-left:0px;
}
#footer-links > div {
margin-right: 10px;
width: 150px;
}
#footer-links .gumtree-elsewhere {
width: 120px;
}
#footer .social-facebook,
#footer .social-twitter,
#footer .social-google,
#footer .social-pinterest,
#footer .social-youtube{ display:block; margin-bottom:3px; height:18px; line-height:18px; padding-left:20px; background-repeat:no-repeat; background-position:left center; background-size:18px 18px; }
</style>
<div id="footer" class="footer">
<div id="footer-links" class="container">
<div class="gumtree-legal" style="display:inline">
<h3><a href="http://www.gumtree.pl">
<img src="http://pic.classistatic.com/image/site/au/global_footer/footer_logo.gif" border="0" alt=""></a></h3>
</div>
<div class="get-to-know-us">
<h3>Poznaj nas</h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=122">O Gumtree</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?category=5">Zasady zamieszczania ogłoszeń</a></li>
</ul>
</div>
<div class="explore-gumtree">
<h3>Odkryj więcej</h3>
<ul>
<li><a href="http://info.gumtree.pl/promowanie/index.html">Promowanie ogłoszeń</a></li>
<li><a href="http://www.gumtree.pl/c-PopularSearches">Popularne wyszukiwania</a></li>
</ul>
</div>
<div class="legalbits">
<h3>Sprawy prawne</h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=120">Zasady korzystania</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=121">Polityka Prywatności</a></li>
</ul>
</div>
<div class="tips-help">
<h3>Pomoc i porady </h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php">Pomoc</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?category=7">Pozostań bezpiecznym </a></li>
<li><a href="http://gumtreehelp.com/pl/index.php">Napisz do nas </a></li>
<li><a href="http://blog.gumtree.pl/">Gumtree Blog </a></li>
</ul>
</div>
<div class="gumtree-elsewhere">
<h3>Śledź nas</h3>
<ul>
<li><a class="social-facebook" href="https://www.facebook.com/GumtreePolska" target="_blank">Facebook</a></li>
<li><a class="social-google" href="https://plus.google.com/103950977256553454134/posts" rel="publisher" target="_blank">Google+</a></li>
<li><a class="social-twitter" href="https://twitter.com/gumtreepolska" target="_blank">Twitter</a></li>
<li><a class="social-youtube" href="http://www.youtube.com/user/GumtreePolska" target="_blank">YouTube</a></li>
<li><a class="social-pinterest" href="http://pinterest.com/gumtreepolska" target="_blank">Pinterest</a></li>
</ul>
</div>
<div class="blog-latest">
</div>
</div>
<!-- Start Alexa Certify Javascript -->
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=wS4fj1a4ZP00g+" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
<div id="copyright">&nbsp;</div>
</div>
<div class="cpyrt">
Copyright © 2014 eBay International AG
</div>
</div>
<!-- google_ad_section_end(weight=ignore) -->
</div>
</div>
<!-- Start of HtmlPageTail -->
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/common/common-min.js"></script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/pages/searchAd-min.js"></script>
<script type="text/javascript" language="JavaScript" src="https://www.google.com/jsapi"></script>
<div id="BeCareful" class="layer0">
<div class="layer1">
<div class="layer2">
<div class="layer3">
<div class="layerbox">
<div class="layerContent">
Uważaj, ten ogłoszeniodawca dodał wiele ogłoszeń, które byliśmy zmuszeni usunąć.
</div>
</div>
</div>
</div>
</div>
</div>
<div id="subform" class="modal" style="width:465px;">
<table cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="modalHeading">
<div class="layerTitleText">Powiadomienia na Gumtree</div>
<div class="closeBtn close" title="Close">&nbsp;</div>
</td>
</tr>
<tr class="layerContent">
<td>
<form name="emailsubscriptionform" action="/c-SignupSubscription?A_ForRentBy=ownr&amp;A_NumberRooms=2&amp;Action=3&amp;AdType=2&amp;Location=3200208&amp;UiComponentId=mainSec&amp;maxPrice=1600&amp;maxPriceBackend=160000">
<span id="almostDoneMsg" style="display: none;">Już prawie gotowe!</span>
<span id="confirmSentMsg" style="display: none;">Wysłaliśmy do Ciebie e-mail z potwierdzeniem. Kliknij link załączony w e-mailu, aby zacząć odbierać powiadomienia.</span>
<span id="requestError" style="display: none;">Nie możemy zrealizować Twojego polecenia, spróbuj ponownie...</span>
<center id="mainSec">
<div id="reloadMain">
<input type="hidden" name="CatId" value="9008"/>
<input type="hidden" name="Keyword" value="ruczaj"/>
<table>
<tr>
<td width="5"></td>
<td></td>
<td align="left">
</td>
<td width="5"></td>
</tr>
<tr>
<td width="5"></td>
<td align="right"><span class="alrtlbl">Adres e-mail</span></td>
<td align="left"><input type="textfield" name="Email" size="30"/></td>
<td width="5"></td>
</tr>
<tr>
<td width="5"></td>
<td align="right" class="rtpePd"><span class="alrtlbl">Podaj ponownie adres e-mail</span></td>
<td align="left" class="rtpePd"><input type="textfield" name="RetypeEmail" size="30"/></td>
<td width="5"></td>
</tr>
<tr>
<td width="5"></td>
<td></td>
<td align="left" width="250"><div id="errorContent"></div></td>
<td width="5"></td>
</tr>
<tr>
<td colspan="4" align="center" height="40"><a href="javascript:submitForm('search')"><span class="newButton">&nbsp;&nbsp;Dodaj powiadomienie&nbsp;&nbsp;</span></a></td>
</tr>
<tr>
<td width="5"></td>
<td class="legal" colspan="2">
Klikając przycisk „Dodaj powiadomienie”, wyrażasz zgodę na nasze <a href="http://www.gumtree.pl/p-TermsAndConditions">Zasady korzystania</a> i <a href="http://www.gumtree.pl/p-Privacy">Politykę prywatności</a>.
</td>
<td></td>
<td width="5"></td>
</tr>
</table>
</div>
</center>
</form>
</td>
</tr>
</table>
</div>
<style>
#persistInput.storeMachId {behavior:url(#default#userData);}
</style>
<form id="persistForm">
<input type="hidden" class="storeMachId" id="persistInput"/>
</form>
<script>
Kj.initMachineId({isProduction:true,cookiePath:'http://include.classistatic.com/include/e884/c3js/classifieds/rel1/FLASH/'});
</script>
<!-- CC JS Includes -->
<script type="text/javascript" charset="UTF-8">
//start-CC JS
setTimeout(function(){var a=document.createElement("script");var b=document.getElementsByTagName("script")[0];a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0017/0492.js?"+Math.floor(new Date().getTime()/3600000);a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)},1);_atrk_opts={atrk_acct:"wS4fj1a4ZP00g+",domain:"gumtree.pl",dynamic:true};(function(){var as=document.createElement('script');as.type='text/javascript';as.async=true;as.src="https://d31qbv1cthcecs.cloudfront.net/atrk.js";var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as,s);})();var googletag=googletag||{};googletag.cmd=googletag.cmd||[];(function(){var gads=document.createElement('script');gads.async=true;gads.type='text/javascript';var useSSL='https:'==document.location.protocol;gads.src=(useSSL?'https:':'http:')+'//www.googletagservices.com/tag/js/gpt.js';var node=document.getElementsByTagName('script')[0];node.parentNode.insertBefore(gads,node);})();$(document).ready(function(){pageURL=window.location.href;curLOC=$("#searchLoc_name").text()||"";curLOC=curLOC.replace(/\W+/g,'_');googletag.cmd.push(function(){googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci/mieszkania_i_domy_do_wynaj_cia',[[728,90],[750,200]],'div-gpt-ad-topbanner').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","ruczaj").setTargeting("pos","top").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci/mieszkania_i_domy_do_wynaj_cia',[160,600],'div-gpt-ad-leftskyscraper').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","ruczaj").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci/mieszkania_i_domy_do_wynaj_cia',[728,90],'div-gpt-ad-bottombanner').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","ruczaj").setTargeting("pos","bottom").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci/mieszkania_i_domy_do_wynaj_cia',[728,90],'div-gpt-ad-srp-midbanner').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","ruczaj").setTargeting("pos","middle").setTargeting("dc_ref",pageURL);googletag.pubads().enableSingleRequest();googletag.enableServices();});googletag.cmd.push(function(){googletag.display('div-gpt-ad-topbanner');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-leftskyscraper');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-bottombanner');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-srp-midbanner');});});
//end -CC JS
//start-TAIL JS
Kj.initGA({isGaSiteTrackerId:true,isGaTrackerId:false});$(document).ready(function(){$('.mainTabs a[href$="c-SelectCategory"]').bind('click',function(){Kj.Ga.trackEventsinGA({category:'Header_PostAdTab',action:'Header_PostAdTab_clicked',opt_label:undefined,track_on_area_level:true});});});var catdata="\0030\003Wszystkie kategorie\0030\0031\0030\004\0030-0\003Nieruchomości\0032\0031\0031\0040-0\0030-0_0\003Wszystkie Nieruchomości\0032\0031\0030\0040-0\0030-0_1\003pokoje do wynajęcia\0039000\0031\0031\0040-0\0030-0_2\003mieszkania i domy do wynajęcia\0039008\0031\0031\0040-0\0030-0_3\003mieszkania i domy - sprzedam i kupię\0039073\0031\0031\0040-0\0030-0_4\003działki\0039194\0031\0031\0040-0\0030-0_5\003krótki termin i noclegi\0039074\0031\0031\0040-0\0030-0_6\003kwatery i domki letniskowe\0039193\0031\0031\0040-0\0030-0_7\003lokal i biuro\0039072\0031\0031\0040-0\0030-0_8\003parking i garaż\0039071\0031\0031\004\0030-1\003Motoryzacja\0035\0031\0031\0040-1\0030-1_0\003Wszystkie Motoryzacja\0035\0031\0030\0040-1\0030-1_1\003samochody osobowe\0039026\0031\0031\0040-1\0030-1_2\003samochody dostawcze\0039027\0031\0031\0040-1\0030-1_3\003motocykle i skutery\0039028\0031\0031\0040-1\0030-1_4\003ciągniki i maszyny rolnicze\0039154\0031\0031\0040-1\0030-1_5\003przyczepy i naczepy\0039155\0031\0031\0040-1\0030-1_6\003części i akcesoria\0039029\0031\0031\004\0030-2\003Łodzie i Pojazdy wodne\0039218\0031\0031\0040-2\0030-2_0\003Wszystkie Łodzie i Pojazdy wodne\0039218\0031\0030\0040-2\0030-2_1\003motorówki\0039219\0031\0031\0040-2\0030-2_2\003skutery wodne\0039222\0031\0031\0040-2\0030-2_3\003żaglówki\0039221\0031\0031\0040-2\0030-2_4\003kajaki i pontony\0039220\0031\0031\0040-2\0030-2_5\003silniki do łodzi\0039223\0031\0031\0040-2\0030-2_6\003akcesoria do łodzi\0039224\0031\0031\0040-2\0030-2_7\003inne pojazdy wodne\0039225\0031\0031\0040-2\0030-2_8\003łodzie wiosłowe\0039226\0031\0031\004\0030-3\003Sprzedam\0034\0031\0031\0040-3\0030-3_0\003Wszystkie Sprzedam\0034\0031\0030\0040-3\0030-3_1\003AGD\0039366\0031\0031\0040-3\0030-3_2\003antyki i kolekcje\0039351\0031\0031\0040-3\0030-3_3\003meble\0039376\0031\0031\0040-3\0030-3_4\003narzędzia i materiały budowlane\0039384\0031\0031\0040-3\0030-3_5\003ogród\0039398\0031\0031\0040-3\0030-3_6\003produkty żywnościowe\0039407\0031\0031\0040-3\0030-3_7\003wyposażenie wnętrz\0039408\0031\0031\0040-3\0030-3_8\003zdrowie\0039418\0031\0031\0040-3\0030-3_9\003sprzedam inne\0039023\0031\0031\004\0030-4\003Elektronika\0039237\0031\0031\0040-4\0030-4_0\003Wszystkie Elektronika\0039237\0031\0030\0040-4\0030-4_1\003audio i hi-fi\0039260\0031\0031\0040-4\0030-4_2\003cesje\0039353\0031\0031\0040-4\0030-4_3\003fotografia i video\0039281\0031\0031\0040-4\0030-4_4\003gry video i konsole\0039265\0031\0031\0040-4\0030-4_5\003komputery i software\0039238\0031\0031\0040-4\0030-4_6\003radiokomunikacja\0039352\0031\0031\0040-4\0030-4_7\003tablety i bookreadery\0039259\0031\0031\0040-4\0030-4_8\003telefony i akcesoria\0039247\0031\0031\0040-4\0030-4_9\003telewizory i odtwarzacze\0039276\0031\0031\0040-4\0030-4_10\003elektronika inne\0039286\0031\0031\004\0030-5\003Dla Dziecka\0039459\0031\0031\0040-5\0030-5_0\003Wszystkie Dla Dziecka\0039459\0031\0030\0040-5\0030-5_1\003artykuły szkolne\0039468\0031\0031\0040-5\0030-5_2\003bezpieczeństwo i zdrowie dziecka\0039460\0031\0031\0040-5\0030-5_3\003buty dla dzieci\0039461\0031\0031\0040-5\0030-5_4\003chrzciny, komunie, imprezy\0039469\0031\0031\0040-5\0030-5_5\003ciąża i karmienie\0039464\0031\0031\0040-5\0030-5_6\003foteliki - nosidełka\0039462\0031\0031\0040-5\0030-5_7\003kąpiel i zdrowie\0039470\0031\0031\0040-5\0030-5_8\003kojce i chodziki\0039471\0031\0031\0040-5\0030-5_9\003meble i wystrój pokoju\0039463\0031\0031\0040-5\0030-5_10\003rowerki i inne pojazdy\0039472\0031\0031\0040-5\0030-5_11\003odzież dziecięca\0039465\0031\0031\0040-5\0030-5_12\003wózki dla dzieci\0039466\0031\0031\0040-5\0030-5_13\003zabawki\0039467\0031\0031\0040-5\0030-5_14\003inne dla dziecka\0039489\0031\0031\004\0030-6\003Sport i Rozrywka\0039490\0031\0031\0040-6\0030-6_0\003Wszystkie Sport i Rozrywka\0039490\0031\0030\0040-6\0030-6_1\003bilety\0039491\0031\0031\0040-6\0030-6_2\003instrumenty i akcesoria muzyczne\0039496\0031\0031\0040-6\0030-6_3\003komiksy i czasopisma\0039497\0031\0031\0040-6\0030-6_4\003książki\0039498\0031\0031\0040-6\0030-6_5\003CD, kasety i płyty\0039514\0031\0031\0040-6\0030-6_6\003filmy i DVD\0039513\0031\0031\0040-6\0030-6_7\003gry planszowe i puzzle\0039515\0031\0031\0040-6\0030-6_8\003sport\0039519\0031\0031\0040-6\0030-6_9\003sprzęt turystyczny\0039531\0031\0031\004\0030-7\003Zwierzaki\0039124\0031\0031\0040-7\0030-7_0\003Wszystkie Zwierzaki\0039124\0031\0030\0040-7\0030-7_1\003psy i szczenięta\0039131\0031\0031\0040-7\0030-7_2\003koty i kocięta\0039125\0031\0031\0040-7\0030-7_3\003inne zwierzaki\0039126\0031\0031\0040-7\0030-7_4\003zgubiono lub znaleziono\0039128\0031\0031\0040-7\0030-7_5\003akcesoria dla zwierząt\0039129\0031\0031\0040-7\0030-7_6\003usługi dla zwierząt\0039130\0031\0031\004\0030-8\003Społeczność\0036\0031\0031\0040-8\0030-8_0\003Wszystkie Społeczność\0036\0031\0030\0040-8\0030-8_1\003drobne pytania i hobby\0039030\0031\0031\0040-8\0030-8_2\003sport, taniec i partnerzy do gry\0039032\0031\0031\0040-8\0030-8_3\003zespoły i muzycy\0039033\0031\0031\0040-8\0030-8_4\003wolontariat\0039227\0031\0031\0040-8\0030-8_5\003wydarzenia lokalne\0039228\0031\0031\0040-8\0030-8_6\003wymiana umiejętności\0039035\0031\0031\0040-8\0030-8_7\003zgubiono lub znaleziono\0039036\0031\0031\0040-8\0030-8_8\003przejazdy\0039037\0031\0031\0040-8\0030-8_9\003podróże\0039038\0031\0031\0040-8\0030-8_10\003dziękuję\0039039\0031\0031\0040-8\0030-8_11\003wyznania\0039084\0031\0031\0040-8\0030-8_12\003szukam starych przyjaciół\0039132\0031\0031\004\0030-9\003Oferty Pracy\0038\0031\0031\0040-9\0030-9_0\003Wszystkie Oferty Pracy\0038\0031\0030\0040-9\0030-9_1\003bar, restauracja i gastronomia\0039056\0031\0031\0040-9\0030-9_2\003biuro i administracja\0039052\0031\0031\0040-9\0030-9_3\003praca na budowie i pracownicy fizyczni\0039142\0031\0031\0040-9\0030-9_4\003fachowcy\0039203\0031\0031\0040-9\0030-9_5\003finanse i księgowość\0039050\0031\0031\0040-9\0030-9_6\003grafika i web design\0039140\0031\0031\0040-9\0030-9_7\003hostessy, modele i aktorzy\0039141\0031\0031\0040-9\0030-9_8\003hr, kadry i rekrutacja\0039053\0031\0031\0040-9\0030-9_9\003inżynierowie, technicy i architekci\0039094\0031\0031\0040-9\0030-9_10\003kierowcy i kurierzy\0039097\0031\0031\0040-9\0030-9_11\003kontrola i inwentaryzacja\0039208\0031\0031\0040-9\0030-9_12\003krawiectwo i moda\0039204\0031\0031\0040-9\0030-9_13\003marketing, media i pr\0039048\0031\0031\0040-9\0030-9_14\003praca typu mlm\0039532\0031\0031\0040-9\0030-9_15\003nauczyciele i edukacja\0039060\0031\0031\0040-9\0030-9_16\003ochrona\0039200\0031\0031\0040-9\0030-9_17\003opiekunki i nianie\0039059\0031\0031\0040-9\0030-9_18\003pielęgnacja i uroda\0039054\0031\0031\0040-9\0030-9_19\003praca dla studentów\0039206\0031\0031\0040-9\0030-9_20\003praca w hotelu\0039058\0031\0031\0040-9\0030-9_21\003prawo i prokuratura\0039049\0031\0031\0040-9\0030-9_22\003programiści, informatyka i internet\0039005\0031\0031\0040-9\0030-9_23\003służba zdrowia i farmacja\0039055\0031\0031\0040-9\0030-9_24\003spedycja\0039205\0031\0031\0040-9\0030-9_25\003sport i fitness\0039202\0031\0031\0040-9\0030-9_26\003sprzątanie i pomoc domowa\0039138\0031\0031\0040-9\0030-9_27\003sprzedaż, handel i praca w sklepie\0039061\0031\0031\0040-9\0030-9_28\003telemarketing i call center\0039098\0031\0031\0040-9\0030-9_29\003turystyka\0039207\0031\0031\0040-9\0030-9_30\003ulotki\0039201\0031\0031\0040-9\0030-9_31\003weterynaria i rolnictwo\0039095\0031\0031\0040-9\0030-9_32\003video i fotografia\0039212\0031\0031\0040-9\0030-9_33\003praca inne\0039099\0031\0031\004\0030-10\003Szukający Zatrudnienia\0039290\0031\0031\0040-10\0030-10_0\003Wszystkie Szukający Zatrudnienia\0039290\0031\0030\0040-10\0030-10_1\003gastronomia\0039291\0031\0031\0040-10\0030-10_2\003biuro i administracja\0039292\0031\0031\0040-10\0030-10_3\003pracownicy fizyczni\0039293\0031\0031\0040-10\0030-10_4\003specjaliści i technicy\0039294\0031\0031\0040-10\0030-10_5\003kierowcy i kurierzy\0039300\0031\0031\0040-10\0030-10_6\003marketing i reklama\0039304\0031\0031\0040-10\0030-10_7\003opiekunki i edukacja\0039305\0031\0031\0040-10\0030-10_8\003ochrona\0039306\0031\0031\0040-10\0030-10_9\003pielęgnacja i uroda\0039308\0031\0031\0040-10\0030-10_10\003sprzedaż i praca w sklepie\0039311\0031\0031\0040-10\0030-10_11\003szukam pracy studenckiej\0039309\0031\0031\0040-10\0030-10_12\003turystyka\0039312\0031\0031\0040-10\0030-10_13\003pozostałe\0039313\0031\0031\004\0030-11\003Usługi\0039\0031\0031\0040-11\0030-11_0\003Wszystkie Usługi\0039\0031\0030\0040-11\0030-11_1\003biura podróży\0039150\0031\0031\0040-11\0030-11_2\003współpraca biznesowa\0039325\0031\0031\0040-11\0030-11_3\003catering\0039554\0031\0031\0040-11\0030-11_4\003usługi finansowe\0039066\0031\0031\0040-11\0030-11_5\003fotografia i video\0039146\0031\0031\0040-11\0030-11_6\003graficy i usługi IT\0039234\0031\0031\0040-11\0030-11_7\003hurt i handel\0039065\0031\0031\0040-11\0030-11_8\003komputery serwis i handel\0039102\0031\0031\0040-11\0030-11_9\003usługi kurierskie\0039337\0031\0031\0040-11\0030-11_10\003nauka i edukacja\0039063\0031\0031\0040-11\0030-11_11\003mechanika i autoskup\0039145\0031\0031\0040-11\0030-11_12\003media i reklama\0039217\0031\0031\0040-11\0030-11_13\003muzycy i artyści\0039148\0031\0031\0040-11\0030-11_14\003ogrodnictwo\0039214\0031\0031\0040-11\0030-11_15\003opieka i agencje niań\0039152\0031\0031\0040-11\0030-11_16\003pielęgnacja i uroda\0039064\0031\0031\0040-11\0030-11_17\003usługi prawne\0039233\0031\0031\0040-11\0030-11_18\003przeprowadzki\0039144\0031\0031\0040-11\0030-11_19\003remont i budowa\0039101\0031\0031\0040-11\0030-11_20\003serwis i montaż\0039236\0031\0031\0040-11\0030-11_21\003sport i fitness\0039151\0031\0031\0040-11\0030-11_22\003sprzątanie\0039149\0031\0031\0040-11\0030-11_23\003śluby, wesela i przyjęcia\0039104\0031\0031\0040-11\0030-11_24\003taxi i przewozy osobowe\0039147\0031\0031\0040-11\0030-11_25\003telefony\0039341\0031\0031\0040-11\0030-11_26\003tłumaczenia i redakcja tekstu\0039216\0031\0031\0040-11\0030-11_27\003utylizacja\0039213\0031\0031\0040-11\0030-11_28\003wypożyczalnie\0039215\0031\0031\0040-11\0030-11_29\003zdrowie\0039235\0031\0031\0040-11\0030-11_30\003inne usługi\0039105\0031\0031\004\0030-12\003Moda\0039541\0031\0031\0040-12\0030-12_0\003Wszystkie Moda\0039541\0031\0030\0040-12\0030-12_1\003akcesoria i galanteria\0039542\0031\0031\0040-12\0030-12_2\003biżuteria i zegarki\0039563\0031\0031\0040-12\0030-12_3\003kosmetyki i perfumy\0039544\0031\0031\0040-12\0030-12_4\003obuwie damskie\0039596\0031\0031\0040-12\0030-12_5\003obuwie męskie\0039604\0031\0031\0040-12\0030-12_6\003odzież damska\0039565\0031\0031\0040-12\0030-12_7\003odzież męska\0039584\0031\0031\0040-12\0030-12_8\003pasmanteria\0039549\0031\0031\0040-12\0030-12_9\003torebki i torby\0039551\0031\0031\0040-12\0030-12_10\003walizki i plecaki\0039552\0031\0031\0040-12\0030-12_11\003inne ubrania\0039553\0031\0031\004";$().ready(function(){$("#searchCat").kjmenu_makeMenu({data:catdata,cssWrapperClass:'nationalSite',OnSelect:function(mitem){$("#searchCat_name").html(mitem.name+"<img border='0' src='http://pic.classistatic.com/image/pics/classifieds/spacer.gif' width='25px' height='1px'/></div>");document.frmSearchAd.CatId.value=mitem.value;$('.sfsp').remove();$('.sfasp').remove();}});});var sdata="\0030\003Polska\003202\0031\0030\004\0030-0\003Dolnośląskie\0033200007\0031\0031\0040-0\0030-0_0\003Wszystkie Dolnośląskie\0033200007\0031\0030\0040-0\0030-0_1\003Bielawa\0033200085\0031\0031\0040-0\0030-0_2\003 Bierutów\0033200435\0031\0031\0040-0\0030-0_3\003Bogatynia\0033200086\0031\0031\0040-0\0030-0_4\003 Boguszów-Gorce\0033200437\0031\0031\0040-0\0030-0_5\003Bolesławiec\0033200087\0031\0031\0040-0\0030-0_6\003 Bolków\0033200436\0031\0031\0040-0\0030-0_7\003 Brzeg Dolny\0033200438\0031\0031\0040-0\0030-0_8\003 Bystrzyca Kłodzka\0033200439\0031\0031\0040-0\0030-0_9\003 Chocianów\0033200440\0031\0031\0040-0\0030-0_10\003 Chojnów\0033200441\0031\0031\0040-0\0030-0_11\003Dzierżoniów\0033200088\0031\0031\0040-0\0030-0_12\003Głogów\0033200089\0031\0031\0040-0\0030-0_13\003Góra\0033200090\0031\0031\0040-0\0030-0_14\003 Gryfów Śląski\0033200442\0031\0031\0040-0\0030-0_15\003Jawor\0033200091\0031\0031\0040-0\0030-0_16\003 Jelcz-Laskowice\0033200443\0031\0031\0040-0\0030-0_17\003Jelenia Góra\0033200092\0031\0031\0040-0\0030-0_18\003Kamienna Góra\0033200093\0031\0031\0040-0\0030-0_19\003Karpacz\0033200094\0031\0031\0040-0\0030-0_20\003Kłodzko\0033200095\0031\0031\0040-0\0030-0_21\003 Kowary\0033200444\0031\0031\0040-0\0030-0_22\003 Kudowa-Zdrój\0033200445\0031\0031\0040-0\0030-0_23\003Legnica\0033200096\0031\0031\0040-0\0030-0_24\003Lubań\0033200097\0031\0031\0040-0\0030-0_25\003Lubin\0033200098\0031\0031\0040-0\0030-0_26\003Lwówek Śląski\0033200099\0031\0031\0040-0\0030-0_27\003Milicz\0033200100\0031\0031\0040-0\0030-0_28\003Nowa Ruda\0033200101\0031\0031\0040-0\0030-0_29\003 Oborniki Śląskie\0033200446\0031\0031\0040-0\0030-0_30\003Oława\0033200102\0031\0031\0040-0\0030-0_31\003Oleśnica\0033200103\0031\0031\0040-0\0030-0_32\003Piechowice\0033200434\0031\0031\0040-0\0030-0_33\003 Pieszyce\0033200447\0031\0031\0040-0\0030-0_34\003 Piława Górna\0033200448\0031\0031\0040-0\0030-0_35\003Polanica-Zdrój\0033200104\0031\0031\0040-0\0030-0_36\003Polkowice\0033200105\0031\0031\0040-0\0030-0_37\003 Strzegom\0033200449\0031\0031\0040-0\0030-0_38\003Strzelin\0033200107\0031\0031\0040-0\0030-0_39\003 Syców\0033200450\0031\0031\0040-0\0030-0_40\003Szklarska Poręba\0033200106\0031\0031\0040-0\0030-0_41\003Środa Śląska\0033200108\0031\0031\0040-0\0030-0_42\003Świdnica\0033200109\0031\0031\0040-0\0030-0_43\003Świebodzice\0033200110\0031\0031\0040-0\0030-0_44\003Trzebnica\0033200111\0031\0031\0040-0\0030-0_45\003Wałbrzych\0033200112\0031\0031\0040-0\0030-0_46\003Wołów\0033200113\0031\0031\0040-0\0030-0_47\003Wrocław\0033200114\0031\0031\0040-0\0030-0_48\003Ząbkowice Śląskie\0033200115\0031\0031\0040-0\0030-0_49\003Zgorzelec\0033200116\0031\0031\0040-0\0030-0_50\003 Ziębice\0033200451\0031\0031\0040-0\0030-0_51\003Złotoryja\0033200117\0031\0031\0040-0\0030-0_52\003 Żarów\0033200452\0031\0031\0040-0\0030-0_53\003 Żmigród\0033200453\0031\0031\004\0030-1\003Kujawsko - pomorskie\0033200075\0031\0031\0040-1\0030-1_0\003Wszystkie Kujawsko - pomorskie\0033200075\0031\0030\0040-1\0030-1_1\003Aleksandrów Kujawski\0033200118\0031\0031\0040-1\0030-1_2\003 Barcin\0033200454\0031\0031\0040-1\0030-1_3\003Brodnica\0033200119\0031\0031\0040-1\0030-1_4\003Bydgoszcz\0033200120\0031\0031\0040-1\0030-1_5\003Chełmno\0033200121\0031\0031\0040-1\0030-1_6\003 Chełmża\0033200455\0031\0031\0040-1\0030-1_7\003 Ciechocinek\0033200456\0031\0031\0040-1\0030-1_8\003 Gniewkowo\0033200457\0031\0031\0040-1\0030-1_9\003Golub-Dobrzyń\0033200122\0031\0031\0040-1\0030-1_10\003Grudziądz\0033200123\0031\0031\0040-1\0030-1_11\003Inowrocław\0033200124\0031\0031\0040-1\0030-1_12\003 Janikowo\0033200458\0031\0031\0040-1\0030-1_13\003 Koronowo\0033200459\0031\0031\0040-1\0030-1_14\003 Kruszwica\0033200460\0031\0031\0040-1\0030-1_15\003Lipno\0033200125\0031\0031\0040-1\0030-1_16\003Mogilno\0033200126\0031\0031\0040-1\0030-1_17\003Nakło nad Notecią\0033200127\0031\0031\0040-1\0030-1_18\003Radziejów\0033200128\0031\0031\0040-1\0030-1_19\003Rypin\0033200129\0031\0031\0040-1\0030-1_20\003Sępólno Krajeńskie\0033200130\0031\0031\0040-1\0030-1_21\003 Solec Kujawski\0033200461\0031\0031\0040-1\0030-1_22\003 Strzelno\0033200462\0031\0031\0040-1\0030-1_23\003Świecie\0033200131\0031\0031\0040-1\0030-1_24\003 Szubin\0033200463\0031\0031\0040-1\0030-1_25\003Toruń\0033200132\0031\0031\0040-1\0030-1_26\003Tuchola\0033200133\0031\0031\0040-1\0030-1_27\003Wąbrzeźno\0033200134\0031\0031\0040-1\0030-1_28\003 Więcbork\0033200464\0031\0031\0040-1\0030-1_29\003Włocławek\0033200135\0031\0031\0040-1\0030-1_30\003Żnin\0033200136\0031\0031\004\0030-2\003Lubelskie\0033200076\0031\0031\0040-2\0030-2_0\003Wszystkie Lubelskie\0033200076\0031\0030\0040-2\0030-2_1\003Bełżyce\0033200465\0031\0031\0040-2\0030-2_2\003Biała Podlaska\0033200137\0031\0031\0040-2\0030-2_3\003Biłgoraj\0033200138\0031\0031\0040-2\0030-2_4\003Chełm\0033200139\0031\0031\0040-2\0030-2_5\003Dęblin\0033200466\0031\0031\0040-2\0030-2_6\003Hrubieszów\0033200140\0031\0031\0040-2\0030-2_7\003Janów Lubelski\0033200141\0031\0031\0040-2\0030-2_8\003Krasnystaw\0033200142\0031\0031\0040-2\0030-2_9\003Kraśnik\0033200143\0031\0031\0040-2\0030-2_10\003Lubartów\0033200144\0031\0031\0040-2\0030-2_11\003Lublin\0033200145\0031\0031\0040-2\0030-2_12\003Łęczna\0033200146\0031\0031\0040-2\0030-2_13\003Łuków\0033200147\0031\0031\0040-2\0030-2_14\003Międzyrzec Podlaski\0033200467\0031\0031\0040-2\0030-2_15\003Opole Lubelskie\0033200148\0031\0031\0040-2\0030-2_16\003Parczew\0033200149\0031\0031\0040-2\0030-2_17\003Poniatowa\0033200468\0031\0031\0040-2\0030-2_18\003Puławy\0033200150\0031\0031\0040-2\0030-2_19\003Radzyń Podlaski\0033200151\0031\0031\0040-2\0030-2_20\003Ryki\0033200152\0031\0031\0040-2\0030-2_21\003Świdnik\0033200153\0031\0031\0040-2\0030-2_22\003Terespol\0033200469\0031\0031\0040-2\0030-2_23\003Tomaszów Lubelski\0033200154\0031\0031\0040-2\0030-2_24\003Włodawa\0033200155\0031\0031\0040-2\0030-2_25\003Zamość\0033200156\0031\0031\004\0030-3\003Lubuskie\0033200077\0031\0031\0040-3\0030-3_0\003Wszystkie Lubuskie\0033200077\0031\0030\0040-3\0030-3_1\003Drezdenko\0033200158\0031\0031\0040-3\0030-3_2\003Gorzów Wielkopolski\0033200157\0031\0031\0040-3\0030-3_3\003Gubin\0033200159\0031\0031\0040-3\0030-3_4\003 Kostrzyn nad Odrą\0033200470\0031\0031\0040-3\0030-3_5\003 Kożuchów\0033200471\0031\0031\0040-3\0030-3_6\003Krosno Odrzańskie\0033200160\0031\0031\0040-3\0030-3_7\003Lubsko\0033200161\0031\0031\0040-3\0030-3_8\003Międzyrzecz\0033200162\0031\0031\0040-3\0030-3_9\003Nowa Sól\0033200163\0031\0031\0040-3\0030-3_10\003 Rzepin\0033200472\0031\0031\0040-3\0030-3_11\003sulechów\0033200166\0031\0031\0040-3\0030-3_12\003Słubice\0033200164\0031\0031\0040-3\0030-3_13\003Strzelce Krajeńskie\0033200165\0031\0031\0040-3\0030-3_14\003 Skwierzyna\0033200473\0031\0031\0040-3\0030-3_15\003Sulęcin\0033200167\0031\0031\0040-3\0030-3_16\003Szprotawa\0033200168\0031\0031\0040-3\0030-3_17\003Świebodzin\0033200169\0031\0031\0040-3\0030-3_18\003 Witnica\0033200474\0031\0031\0040-3\0030-3_19\003Wschowa\0033200170\0031\0031\0040-3\0030-3_20\003Zielona Góra\0033200171\0031\0031\0040-3\0030-3_21\003Żagań\0033200172\0031\0031\0040-3\0030-3_22\003Żary\0033200173\0031\0031\004\0030-4\003Łódzkie\0033200004\0031\0031\0040-4\0030-4_0\003Wszystkie Łódzkie\0033200004\0031\0030\0040-4\0030-4_1\003Aleksandrów Łódzki\0033200174\0031\0031\0040-4\0030-4_2\003Bełchatów\0033200175\0031\0031\0040-4\0030-4_3\003Brzeziny\0033200176\0031\0031\0040-4\0030-4_4\003Głowno\0033200177\0031\0031\0040-4\0030-4_5\003 Koluszki\0033200475\0031\0031\0040-4\0030-4_6\003Konstantynów Łódzki\0033200178\0031\0031\0040-4\0030-4_7\003Kutno\0033200179\0031\0031\0040-4\0030-4_8\003Łask\0033200180\0031\0031\0040-4\0030-4_9\003Łęczyca\0033200181\0031\0031\0040-4\0030-4_10\003Łowicz\0033200182\0031\0031\0040-4\0030-4_11\003Łódź\0033200183\0031\0031\0040-4\0030-4_12\003Opoczno\0033200184\0031\0031\0040-4\0030-4_13\003Ozorków\0033200185\0031\0031\0040-4\0030-4_14\003Pabianice\0033200186\0031\0031\0040-4\0030-4_15\003Pajęczno\0033200187\0031\0031\0040-4\0030-4_16\003Piotrków Trybunalski\0033200188\0031\0031\0040-4\0030-4_17\003Poddębice\0033200189\0031\0031\0040-4\0030-4_18\003Radomsko\0033200190\0031\0031\0040-4\0030-4_19\003Rawa Mazowiecka\0033200191\0031\0031\0040-4\0030-4_20\003Sieradz\0033200192\0031\0031\0040-4\0030-4_21\003Skierniewice\0033200193\0031\0031\0040-4\0030-4_22\003 Tuszyn\0033200476\0031\0031\0040-4\0030-4_23\003Tomaszów Mazowiecki\0033200194\0031\0031\0040-4\0030-4_24\003Wieluń\0033200195\0031\0031\0040-4\0030-4_25\003Wieruszów\0033200196\0031\0031\0040-4\0030-4_26\003Zduńska Wola\0033200197\0031\0031\0040-4\0030-4_27\003 Zelów\0033200477\0031\0031\0040-4\0030-4_28\003Zgierz\0033200198\0031\0031\0040-4\0030-4_29\003 Żychlin\0033200478\0031\0031\004\0030-5\003Małopolskie\0033200003\0031\0031\0040-5\0030-5_0\003Wszystkie Małopolskie\0033200003\0031\0030\0040-5\0030-5_1\003Andrychów\0033200199\0031\0031\0040-5\0030-5_2\003Bochnia\0033200200\0031\0031\0040-5\0030-5_3\003Brzesko\0033200201\0031\0031\0040-5\0030-5_4\003Brzeszcze\0033200479\0031\0031\0040-5\0030-5_5\003Bukowina Tatrzańska\0033200202\0031\0031\0040-5\0030-5_6\003Bukowno\0033200480\0031\0031\0040-5\0030-5_7\003Chełmek\0033200481\0031\0031\0040-5\0030-5_8\003Chrzanów\0033200203\0031\0031\0040-5\0030-5_9\003Dąbrowa Tarnowska\0033200204\0031\0031\0040-5\0030-5_10\003Gorlice\0033200205\0031\0031\0040-5\0030-5_11\003Kęty\0033200206\0031\0031\0040-5\0030-5_12\003Kościelisko\0033200207\0031\0031\0040-5\0030-5_13\003Kraków\0033200208\0031\0031\0040-5\0030-5_14\003Krościenko nad Dunajcem\0033200491\0031\0031\0040-5\0030-5_15\003Krynica-Zdrój\0033200209\0031\0031\0040-5\0030-5_16\003Krzeszowice\0033200482\0031\0031\0040-5\0030-5_17\003Libiąż\0033200483\0031\0031\0040-5\0030-5_18\003Limanowa\0033200210\0031\0031\0040-5\0030-5_19\003Miechów\0033200211\0031\0031\0040-5\0030-5_20\003Mszana Dolna\0033200484\0031\0031\0040-5\0030-5_21\003Myślenice\0033200212\0031\0031\0040-5\0030-5_22\003Niepołomice\0033200485\0031\0031\0040-5\0030-5_23\003Nowy Sącz\0033200213\0031\0031\0040-5\0030-5_24\003Nowy Targ\0033200214\0031\0031\0040-5\0030-5_25\003Olkusz\0033200215\0031\0031\0040-5\0030-5_26\003Oświęcim\0033200216\0031\0031\0040-5\0030-5_27\003Piwniczna-Zdrój\0033200486\0031\0031\0040-5\0030-5_28\003Proszowice\0033200217\0031\0031\0040-5\0030-5_29\003Rabka-Zdrój\0033200487\0031\0031\0040-5\0030-5_30\003Skawina\0033200218\0031\0031\0040-5\0030-5_31\003Stary Sącz\0033200488\0031\0031\0040-5\0030-5_32\003Sucha Beskidzka\0033200219\0031\0031\0040-5\0030-5_33\003Szczawnica\0033200220\0031\0031\0040-5\0030-5_34\003Tarnów\0033200221\0031\0031\0040-5\0030-5_35\003Trzebinia\0033200222\0031\0031\0040-5\0030-5_36\003Tuchów\0033200489\0031\0031\0040-5\0030-5_37\003Wadowice\0033200223\0031\0031\0040-5\0030-5_38\003Wieliczka\0033200224\0031\0031\0040-5\0030-5_39\003Wolbrom\0033200490\0031\0031\0040-5\0030-5_40\003Zakopane\0033200225\0031\0031\004\0030-6\003Mazowieckie\0033200001\0031\0031\0040-6\0030-6_0\003Wszystkie Mazowieckie\0033200001\0031\0030\0040-6\0030-6_1\003Warszawa\0033200008\0031\0031\0040-6\0030-6_2\003Północne powiaty\0033200027\0031\0031\0040-6\0030-6_3\003Pn - wsch powiaty\0033200036\0031\0031\0040-6\0030-6_4\003Pn - zach powiaty\0033200041\0031\0031\0040-6\0030-6_5\003Południowe powiaty\0033200042\0031\0031\0040-6\0030-6_6\003Pd - wsch powiaty\0033200043\0031\0031\0040-6\0030-6_7\003Pd - zach powiaty\0033200044\0031\0031\0040-6\0030-6_8\003Wschodnie powiaty\0033200045\0031\0031\0040-6\0030-6_9\003Zachodnie powiaty\0033200046\0031\0031\004\0030-7\003Opolskie\0033200078\0031\0031\0040-7\0030-7_0\003Wszystkie Opolskie\0033200078\0031\0030\0040-7\0030-7_1\003Brzeg\0033200226\0031\0031\0040-7\0030-7_2\003Głubczyce\0033200227\0031\0031\0040-7\0030-7_3\003Grodków\0033200526\0031\0031\0040-7\0030-7_4\003Kędzierzyn-Koźle\0033200228\0031\0031\0040-7\0030-7_5\003Kluczbork\0033200229\0031\0031\0040-7\0030-7_6\003Krapkowice\0033200230\0031\0031\0040-7\0030-7_7\003Namysłów\0033200231\0031\0031\0040-7\0030-7_8\003Niemodlin\0033200527\0031\0031\0040-7\0030-7_9\003Nysa\0033200232\0031\0031\0040-7\0030-7_10\003Olesno\0033200233\0031\0031\0040-7\0030-7_11\003Opole\0033200234\0031\0031\0040-7\0030-7_12\003Ozimek\0033200528\0031\0031\0040-7\0030-7_13\003Paczków\0033200529\0031\0031\0040-7\0030-7_14\003Praszka\0033200530\0031\0031\0040-7\0030-7_15\003Prudnik\0033200235\0031\0031\0040-7\0030-7_16\003Strzelce Opolskie\0033200236\0031\0031\0040-7\0030-7_17\003Zawadzkie\0033200531\0031\0031\0040-7\0030-7_18\003Zdzieszowice\0033200532\0031\0031\004\0030-8\003Podkarpackie\0033200079\0031\0031\0040-8\0030-8_0\003Wszystkie Podkarpackie\0033200079\0031\0030\0040-8\0030-8_1\003Brzozów\0033200237\0031\0031\0040-8\0030-8_2\003Dębica\0033200238\0031\0031\0040-8\0030-8_3\003Jarosław\0033200239\0031\0031\0040-8\0030-8_4\003Jasło\0033200240\0031\0031\0040-8\0030-8_5\003Kolbuszowa\0033200241\0031\0031\0040-8\0030-8_6\003Krosno\0033200242\0031\0031\0040-8\0030-8_7\003Lesko\0033200243\0031\0031\0040-8\0030-8_8\003Leżajsk\0033200244\0031\0031\0040-8\0030-8_9\003Lubaczów\0033200245\0031\0031\0040-8\0030-8_10\003Łańcut\0033200246\0031\0031\0040-8\0030-8_11\003Mielec\0033200247\0031\0031\0040-8\0030-8_12\003Nisko\0033200248\0031\0031\0040-8\0030-8_13\003Nowa Dęba\0033200533\0031\0031\0040-8\0030-8_14\003Przemyśl\0033200249\0031\0031\0040-8\0030-8_15\003Przeworsk\0033200250\0031\0031\0040-8\0030-8_16\003Ropczyce\0033200251\0031\0031\0040-8\0030-8_17\003Rzeszów\0033200252\0031\0031\0040-8\0030-8_18\003Sanok\0033200253\0031\0031\0040-8\0030-8_19\003Sędziszów Małopolski\0033200534\0031\0031\0040-8\0030-8_20\003Stalowa Wola\0033200254\0031\0031\0040-8\0030-8_21\003Strzyżów\0033200255\0031\0031\0040-8\0030-8_22\003Tarnobrzeg\0033200256\0031\0031\0040-8\0030-8_23\003Ustrzyki Dolne\0033200257\0031\0031\004\0030-9\003Podlaskie\0033200080\0031\0031\0040-9\0030-9_0\003Wszystkie Podlaskie\0033200080\0031\0030\0040-9\0030-9_1\003Augustów\0033200258\0031\0031\0040-9\0030-9_2\003Białystok\0033200259\0031\0031\0040-9\0030-9_3\003Bielsk Podlaski\0033200260\0031\0031\0040-9\0030-9_4\003 Czarna Białostocka\0033200535\0031\0031\0040-9\0030-9_5\003 Dąbrowa Białostocka\0033200536\0031\0031\0040-9\0030-9_6\003Grajewo\0033200261\0031\0031\0040-9\0030-9_7\003Hajnówka\0033200262\0031\0031\0040-9\0030-9_8\003Kolno\0033200263\0031\0031\0040-9\0030-9_9\003Łapy\0033200264\0031\0031\0040-9\0030-9_10\003Łomża\0033200265\0031\0031\0040-9\0030-9_11\003Mońki\0033200266\0031\0031\0040-9\0030-9_12\003Sejny\0033200267\0031\0031\0040-9\0030-9_13\003Siemiatycze\0033200268\0031\0031\0040-9\0030-9_14\003Sokółka\0033200269\0031\0031\0040-9\0030-9_15\003Suwałki\0033200270\0031\0031\0040-9\0030-9_16\003 Wasilków\0033200537\0031\0031\0040-9\0030-9_17\003Wysokie Mazowieckie\0033200271\0031\0031\0040-9\0030-9_18\003Zambrów\0033200272\0031\0031\004\0030-10\003Pomorskie\0033200005\0031\0031\0040-10\0030-10_0\003Wszystkie Pomorskie\0033200005\0031\0030\0040-10\0030-10_1\003Bytów\0033200407\0031\0031\0040-10\0030-10_2\003Chojnice\0033200408\0031\0031\0040-10\0030-10_3\003Człuchów\0033200409\0031\0031\0040-10\0030-10_4\003Czersk\0033200539\0031\0031\0040-10\0030-10_5\003Gdańsk\0033200072\0031\0031\0040-10\0030-10_6\003Gdynia\0033200073\0031\0031\0040-10\0030-10_7\003Gniew\0033200543\0031\0031\0040-10\0030-10_8\003Hel\0033200410\0031\0031\0040-10\0030-10_9\003Jastarnia\0033200411\0031\0031\0040-10\0030-10_10\003Jastrzębia Góra\0033200412\0031\0031\0040-10\0030-10_11\003Kartuzy\0033200413\0031\0031\0040-10\0030-10_12\003Karwia\0033200414\0031\0031\0040-10\0030-10_13\003Kościerzyna\0033200415\0031\0031\0040-10\0030-10_14\003Krynica Morska\0033200416\0031\0031\0040-10\0030-10_15\003Kwidzyn\0033200417\0031\0031\0040-10\0030-10_16\003Łeba\0033200418\0031\0031\0040-10\0030-10_17\003Lębork\0033200419\0031\0031\0040-10\0030-10_18\003Malbork\0033200420\0031\0031\0040-10\0030-10_19\003Miastko\0033200538\0031\0031\0040-10\0030-10_20\003Nowy Dwór Gdański\0033200421\0031\0031\0040-10\0030-10_21\003Pelplin\0033200541\0031\0031\0040-10\0030-10_22\003Prabuty\0033200540\0031\0031\0040-10\0030-10_23\003Pruszcz Gdański\0033200422\0031\0031\0040-10\0030-10_24\003Puck\0033200423\0031\0031\0040-10\0030-10_25\003Reda\0033200424\0031\0031\0040-10\0030-10_26\003Rumia\0033200425\0031\0031\0040-10\0030-10_27\003Skarszewy\0033200542\0031\0031\0040-10\0030-10_28\003Słupsk\0033200426\0031\0031\0040-10\0030-10_29\003Sopot\0033200074\0031\0031\0040-10\0030-10_30\003Starogard Gdański\0033200427\0031\0031\0040-10\0030-10_31\003Stegna\0033200428\0031\0031\0040-10\0030-10_32\003Sztum\0033200429\0031\0031\0040-10\0030-10_33\003Sztutowo\0033200544\0031\0031\0040-10\0030-10_34\003Tczew\0033200430\0031\0031\0040-10\0030-10_35\003Ustka\0033200431\0031\0031\0040-10\0030-10_36\003Wejherowo\0033200432\0031\0031\0040-10\0030-10_37\003Władysławowo\0033200433\0031\0031\004\0030-11\003Śląskie\0033200002\0031\0031\0040-11\0030-11_0\003Wszystkie Śląskie\0033200002\0031\0030\0040-11\0030-11_1\003Będzin\0033200273\0031\0031\0040-11\0030-11_2\003Bielsko-Biała\0033200274\0031\0031\0040-11\0030-11_3\003Bieruń\0033200275\0031\0031\0040-11\0030-11_4\003 Blachownia\0033200545\0031\0031\0040-11\0030-11_5\003Bytom\0033200277\0031\0031\0040-11\0030-11_6\003Chorzów\0033200278\0031\0031\0040-11\0030-11_7\003Cieszyn\0033200279\0031\0031\0040-11\0030-11_8\003 Czechowice-Dziedzice\0033200546\0031\0031\0040-11\0030-11_9\003 Czeladź\0033200547\0031\0031\0040-11\0030-11_10\003 Czerwionka-Leszczyny\0033200548\0031\0031\0040-11\0030-11_11\003Częstochowa\0033200280\0031\0031\0040-11\0030-11_12\003Dąbrowa Górnicza\0033200281\0031\0031\0040-11\0030-11_13\003Gliwice\0033200282\0031\0031\0040-11\0030-11_14\003 Imielin\0033200549\0031\0031\0040-11\0030-11_15\003Jastrzębie-Zdrój\0033200283\0031\0031\0040-11\0030-11_16\003Jaworzno\0033200284\0031\0031\0040-11\0030-11_17\003 Kalety\0033200550\0031\0031\0040-11\0030-11_18\003 Knurów\0033200551\0031\0031\0040-11\0030-11_19\003Katowice\0033200285\0031\0031\0040-11\0030-11_20\003Kłobuck\0033200286\0031\0031\0040-11\0030-11_21\003 Lędziny\0033200552\0031\0031\0040-11\0030-11_22\003Lubliniec\0033200287\0031\0031\0040-11\0030-11_23\003 Łaziska Górne\0033200553\0031\0031\0040-11\0030-11_24\003Mikołów\0033200288\0031\0031\0040-11\0030-11_25\003Mysłowice\0033200289\0031\0031\0040-11\0030-11_26\003Myszków\0033200290\0031\0031\0040-11\0030-11_27\003 Orzesze\0033200554\0031\0031\0040-11\0030-11_28\003Piekary Śląskie\0033200291\0031\0031\0040-11\0030-11_29\003 Poręba\0033200555\0031\0031\0040-11\0030-11_30\003Pszczyna\0033200292\0031\0031\0040-11\0030-11_31\003 Pszów\0033200556\0031\0031\0040-11\0030-11_32\003 Pyskowice\0033200557\0031\0031\0040-11\0030-11_33\003Racibórz\0033200293\0031\0031\0040-11\0030-11_34\003 Radlin\0033200558\0031\0031\0040-11\0030-11_35\003 Radzionków\0033200559\0031\0031\0040-11\0030-11_36\003Ruda Śląska\0033200294\0031\0031\0040-11\0030-11_37\003Rybnik\0033200295\0031\0031\0040-11\0030-11_38\003 Rydułtowy\0033200560\0031\0031\0040-11\0030-11_39\003Siemianowice Śląskie\0033200296\0031\0031\0040-11\0030-11_40\003 Skoczów\0033200561\0031\0031\0040-11\0030-11_41\003Sosnowiec\0033200297\0031\0031\0040-11\0030-11_42\003Świętochłowice\0033200298\0031\0031\0040-11\0030-11_43\003Szczyrk\0033200299\0031\0031\0040-11\0030-11_44\003Tarnowskie Góry\0033200300\0031\0031\0040-11\0030-11_45\003Tychy\0033200301\0031\0031\0040-11\0030-11_46\003 Ustroń\0033200562\0031\0031\0040-11\0030-11_47\003Wisła\0033200302\0031\0031\0040-11\0030-11_48\003Wodzisław Śląski\0033200303\0031\0031\0040-11\0030-11_49\003 Wojkowice\0033200563\0031\0031\0040-11\0030-11_50\003Zabrze\0033200304\0031\0031\0040-11\0030-11_51\003Zawiercie\0033200305\0031\0031\0040-11\0030-11_52\003Żory\0033200306\0031\0031\0040-11\0030-11_53\003Żywiec\0033200307\0031\0031\004\0030-12\003Świętokrzyskie\0033200082\0031\0031\0040-12\0030-12_0\003Wszystkie Świętokrzyskie\0033200082\0031\0030\0040-12\0030-12_1\003Busko-Zdrój\0033200308\0031\0031\0040-12\0030-12_2\003Jędrzejów\0033200309\0031\0031\0040-12\0030-12_3\003Kazimierza Wielka\0033200310\0031\0031\0040-12\0030-12_4\003Kielce\0033200311\0031\0031\0040-12\0030-12_5\003Końskie\0033200312\0031\0031\0040-12\0030-12_6\003Opatów\0033200313\0031\0031\0040-12\0030-12_7\003Ostrowiec Świętokrzyski\0033200314\0031\0031\0040-12\0030-12_8\003Pińczów\0033200315\0031\0031\0040-12\0030-12_9\003Połaniec\0033200564\0031\0031\0040-12\0030-12_10\003Sandomierz\0033200316\0031\0031\0040-12\0030-12_11\003Skarżysko-Kamienna\0033200317\0031\0031\0040-12\0030-12_12\003Starachowice\0033200318\0031\0031\0040-12\0030-12_13\003Staszów\0033200319\0031\0031\0040-12\0030-12_14\003Suchedniów\0033200565\0031\0031\0040-12\0030-12_15\003Włoszczowa\0033200320\0031\0031\004\0030-13\003Warmińsko-mazurskie\0033200083\0031\0031\0040-13\0030-13_0\003Wszystkie Warmińsko-mazurskie\0033200083\0031\0030\0040-13\0030-13_1\003Bartoszyce\0033200321\0031\0031\0040-13\0030-13_2\003Biskupiec\0033200322\0031\0031\0040-13\0030-13_3\003Braniewo\0033200323\0031\0031\0040-13\0030-13_4\003Dobre Miasto\0033200324\0031\0031\0040-13\0030-13_5\003Działdowo\0033200325\0031\0031\0040-13\0030-13_6\003Elbląg\0033200326\0031\0031\0040-13\0030-13_7\003Ełk\0033200327\0031\0031\0040-13\0030-13_8\003Giżycko\0033200328\0031\0031\0040-13\0030-13_9\003Gołdap\0033200329\0031\0031\0040-13\0030-13_10\003Iława\0033200330\0031\0031\0040-13\0030-13_11\003Kętrzyn\0033200331\0031\0031\0040-13\0030-13_12\003Lidzbark Warmiński\0033200332\0031\0031\0040-13\0030-13_13\003 Lubawa\0033200566\0031\0031\0040-13\0030-13_14\003Mikołajki\0033200333\0031\0031\0040-13\0030-13_15\003 Morąg\0033200567\0031\0031\0040-13\0030-13_16\003Mrągowo\0033200334\0031\0031\0040-13\0030-13_17\003Nidzica\0033200335\0031\0031\0040-13\0030-13_18\003Nowe Miasto Lubawskie\0033200336\0031\0031\0040-13\0030-13_19\003Olecko\0033200337\0031\0031\0040-13\0030-13_20\003Olsztyn\0033200338\0031\0031\0040-13\0030-13_21\003 Olsztynek\0033200568\0031\0031\0040-13\0030-13_22\003 Orneta\0033200569\0031\0031\0040-13\0030-13_23\003Ostróda\0033200339\0031\0031\0040-13\0030-13_24\003 Pasłęk\0033200570\0031\0031\0040-13\0030-13_25\003Pisz\0033200340\0031\0031\0040-13\0030-13_26\003Szczytno\0033200341\0031\0031\0040-13\0030-13_27\003Węgorzewo\0033200342\0031\0031\004\0030-14\003Wielkopolskie\0033200006\0031\0031\0040-14\0030-14_0\003Wszystkie Wielkopolskie\0033200006\0031\0030\0040-14\0030-14_1\003Chodzież\0033200343\0031\0031\0040-14\0030-14_2\003Czarnków\0033200344\0031\0031\0040-14\0030-14_3\003Gniezno\0033200345\0031\0031\0040-14\0030-14_4\003Gostyń\0033200346\0031\0031\0040-14\0030-14_5\003Grodzisk Wielkopolski\0033200347\0031\0031\0040-14\0030-14_6\003Jarocin\0033200348\0031\0031\0040-14\0030-14_7\003Jastrowie\0033200571\0031\0031\0040-14\0030-14_8\003Kalisz\0033200349\0031\0031\0040-14\0030-14_9\003Kępno\0033200350\0031\0031\0040-14\0030-14_10\003Koło\0033200351\0031\0031\0040-14\0030-14_11\003Konin\0033200352\0031\0031\0040-14\0030-14_12\003Kostrzyn\0033200572\0031\0031\0040-14\0030-14_13\003Kościan\0033200353\0031\0031\0040-14\0030-14_14\003Kórnik\0033200573\0031\0031\0040-14\0030-14_15\003Krotoszyn\0033200354\0031\0031\0040-14\0030-14_16\003Leszno\0033200355\0031\0031\0040-14\0030-14_17\003Luboń\0033200356\0031\0031\0040-14\0030-14_18\003Międzychód\0033200357\0031\0031\0040-14\0030-14_19\003Mosina\0033200358\0031\0031\0040-14\0030-14_20\003Murowana Goślina\0033200359\0031\0031\0040-14\0030-14_21\003Nowy Tomyśl\0033200360\0031\0031\0040-14\0030-14_22\003Oborniki\0033200361\0031\0031\0040-14\0030-14_23\003Opalenica\0033200574\0031\0031\0040-14\0030-14_24\003Ostrów Wielkopolski\0033200362\0031\0031\0040-14\0030-14_25\003Ostrzeszów\0033200363\0031\0031\0040-14\0030-14_26\003Piła\0033200364\0031\0031\0040-14\0030-14_27\003Pleszew\0033200365\0031\0031\0040-14\0030-14_28\003Pniewy\0033200575\0031\0031\0040-14\0030-14_29\003Pobiedziska\0033200576\0031\0031\0040-14\0030-14_30\003Poznań\0033200366\0031\0031\0040-14\0030-14_31\003Puszczykowo\0033200577\0031\0031\0040-14\0030-14_32\003Rawicz\0033200367\0031\0031\0040-14\0030-14_33\003Rogoźno\0033200578\0031\0031\0040-14\0030-14_34\003Słupca\0033200368\0031\0031\0040-14\0030-14_35\003Swarzędz\0033200369\0031\0031\0040-14\0030-14_36\003Szamotuły\0033200370\0031\0031\0040-14\0030-14_37\003Śrem\0033200371\0031\0031\0040-14\0030-14_38\003Środa Wielkopolska\0033200372\0031\0031\0040-14\0030-14_39\003Trzcianka\0033200373\0031\0031\0040-14\0030-14_40\003Trzemeszno\0033200579\0031\0031\0040-14\0030-14_41\003Turek\0033200374\0031\0031\0040-14\0030-14_42\003Wągrowiec\0033200375\0031\0031\0040-14\0030-14_43\003Witkowo\0033200580\0031\0031\0040-14\0030-14_44\003Wolsztyn\0033200376\0031\0031\0040-14\0030-14_45\003Wronki\0033200581\0031\0031\0040-14\0030-14_46\003Września\0033200377\0031\0031\0040-14\0030-14_47\003Złotów\0033200378\0031\0031\004\0030-15\003Zachodniopomorskie\0033200084\0031\0031\0040-15\0030-15_0\003Wszystkie Zachodniopomorskie\0033200084\0031\0030\0040-15\0030-15_1\003Barlinek\0033200379\0031\0031\0040-15\0030-15_2\003Białogard\0033200380\0031\0031\0040-15\0030-15_3\003Cedynia\0033200381\0031\0031\0040-15\0030-15_4\003Choszczno\0033200382\0031\0031\0040-15\0030-15_5\003Czaplinek\0033200586\0031\0031\0040-15\0030-15_6\003Darłowo\0033200383\0031\0031\0040-15\0030-15_7\003Dębno\0033200384\0031\0031\0040-15\0030-15_8\003Drawno\0033200385\0031\0031\0040-15\0030-15_9\003Drawsko Pomorskie\0033200386\0031\0031\0040-15\0030-15_10\003Goleniów\0033200387\0031\0031\0040-15\0030-15_11\003Gryfice\0033200388\0031\0031\0040-15\0030-15_12\003Gryfino\0033200389\0031\0031\0040-15\0030-15_13\003Kamień Pomorski\0033200390\0031\0031\0040-15\0030-15_14\003Kołobrzeg\0033200391\0031\0031\0040-15\0030-15_15\003Koszalin\0033200392\0031\0031\0040-15\0030-15_16\003Łobez\0033200393\0031\0031\0040-15\0030-15_17\003Międzyzdroje\0033200394\0031\0031\0040-15\0030-15_18\003Mielno\0033200395\0031\0031\0040-15\0030-15_19\003Myślibórz\0033200396\0031\0031\0040-15\0030-15_20\003Nowogard\0033200397\0031\0031\0040-15\0030-15_21\003Police\0033200398\0031\0031\0040-15\0030-15_22\003Połczyn-Zdrój\0033200582\0031\0031\0040-15\0030-15_23\003Pyrzyce\0033200399\0031\0031\0040-15\0030-15_24\003Sławno\0033200400\0031\0031\0040-15\0030-15_25\003Stargard Szczeciński\0033200401\0031\0031\0040-15\0030-15_26\003Szczecin\0033200402\0031\0031\0040-15\0030-15_27\003Szczecinek\0033200403\0031\0031\0040-15\0030-15_28\003Świdwin\0033200404\0031\0031\0040-15\0030-15_29\003Świnoujście\0033200405\0031\0031\0040-15\0030-15_30\003Trzebiatów\0033200583\0031\0031\0040-15\0030-15_31\003Wałcz\0033200406\0031\0031\0040-15\0030-15_32\003Wolin\0033200584\0031\0031\0040-15\0030-15_33\003Złocieniec\0033200585\0031\0031\004";var provinceSearchInputHtml='<input name="isProvinceSearch" type="hidden" value="true" />';$().ready(function(){function getURLParameter(name){return decodeURIComponent((location.href.match(RegExp("[QQ]"+name+'Z(.+?)(QQ|$)'))||[,null])[1]);}
var isProvinceSearch=getURLParameter('isProvinceSearch');document.frmSearchAd.Location.value=Math.abs(3200208);if(isProvinceSearch=='true'){var isProvinceSearchInput=$('input[name=isProvinceSearch]');if(isProvinceSearchInput.length>0){isProvinceSearchInput.val('true');}
else{$('#frmSearchAd').append(provinceSearchInputHtml);}}
$("#searchLoc").kjmenu_makeMenu({data:sdata,zindex:90000,cssWrapperClass:'nationalSite',OnSelect:function(mitem){var provinceSearchInput=$('input[name=isProvinceSearch]');if(mitem.value<-1){if(provinceSearchInput.length>0){provinceSearchInput.val('true');}
else{$('#frmSearchAd').append(provinceSearchInputHtml);}}
else{if(provinceSearchInput.length>0){provinceSearchInput.remove();}}
$("#searchLoc_name").html(mitem.name+"<img border='0' src='http://pic.classistatic.com/image/pics/classifieds/spacer.gif' width='25px' height='1px'/>");document.frmSearchAd.Location.value=Math.abs(mitem.value);$('.sfsp').remove();}});});addOnUnloadFunction('disableElement("searchAdGo")');var autoOptions={maxChars:4,hideLabel:'Ukryj',timeout:1,maxEntries:7,containerStyleClass:'keySpan',submitOnlick:true,baseUrl:"http://ac.classistatic.com/ac/10028/202/pl_PL/"};$(document).ready(function(){$("input.keyword").autocomplete1(autoOptions);$("#searchAdGo").click(function(){gAnalyticsPushForSearch("Click-Search",$(".newHeader input[name=distance]").val());});$("form#frmSearchAd").submit(function(){if($("#autoComp")[0].value==="Czego szukasz...?"){$("#autoComp")[0].value="";}
$("#searchAdGo").attr("disabled","true");return true;});});function gAnalyticsPushForSearch(srchType,numValue){}
var browsedata="\004\0030\003Nieruchomości\003http://www.gumtree.pl/fp-nieruchomosci/krakow/c2l3200208\004\0030\003Sprzedam\003http://www.gumtree.pl/fp-sprzedam/krakow/c4l3200208\004\0030\003Oferty Pracy\003http://www.gumtree.pl/fp-oferty-pracy/krakow/c8l3200208\004\0030\003Motoryzacja\003http://www.gumtree.pl/fp-motoryzacja/krakow/c5l3200208\004\0030\003Szukający Zatrudnienia\003http://www.gumtree.pl/fp-szukajacy-zatrudnienia/krakow/c9290l3200208\004\0030\003Moda\003http://www.gumtree.pl/fp-moda/krakow/c9541l3200208\004\0030\003Łodzie i Pojazdy wodne\003http://www.gumtree.pl/fp-lodzie-i-pojazdy-wodne/krakow/c9218l3200208\004\0030\003Elektronika\003http://www.gumtree.pl/fp-elektronika/krakow/c9237l3200208\004\0030\003Usługi\003http://www.gumtree.pl/fp-uslugi/krakow/c9l3200208\004\0030\003Dla Dziecka\003http://www.gumtree.pl/fp-dla-dziecka/krakow/c9459l3200208\004\0030\003Zwierzaki\003http://www.gumtree.pl/fp-zwierzaki/krakow/c9124l3200208\004\0030\003Sport i Rozrywka\003http://www.gumtree.pl/fp-sport-i-rozrywka/krakow/c9490l3200208\004\0030\003Społeczność\003http://www.gumtree.pl/fp-spolecznosc/krakow/c6l3200208\004\0030\003Oddam za darmo\003http://www.gumtree.pl/fp-krakow/l3200208?AdType=2&PriceAlternative=3\004\0030\003Wymiana/zamiana\003http://www.gumtree.pl/fp-krakow/l3200208?PriceAlternative=5";$(document).ready(function(){$("#AreaHomeTab,#SiteHomeTab").kjmenu_makeMenu({data:browsedata,OnSelect:function(mitem){document.location.replace(mitem.value);}});$("#changeLocDiv").click(function(){$.ajax({url:'http://www.gumtree.pl/c-GetLocation?CatId=9008&PageName=',dataType:'script'});});});function trackHomeTabDropdown(type){var statisticUrl="";if(type=="tabname"){statisticUrl='http://www.gumtree.pl/c-Statistic?StatType=';}else if(type=="link"){statisticUrl='http://www.gumtree.pl/c-Statistic?StatType=HomeTabDropdownCount';}
statisticUrl=statisticUrl+'&ms='+new Date().getTime();$.get(statisticUrl);return true;}
var KNS=KNS||{};KNS.popWordSel='.floatLeft30px a';KNS.miscLabels=KNS.miscLabels||{};KNS.miscLabels.keyWordsLabelEn="Related";$(document).ready(function(){$(KNS.popWordSel).click(function(){Kj.Ga.trackEventsinGA({category:'Clicks on '+KNS.miscLabels.keyWordsLabelEn+' Searches',action:'clicked word # '+($(KNS.popWordSel).index($(this))+1),opt_label:$(this).attr('href'),track_on_area_level:true});});});$(document).ready(function(){$('.postAdLinkSB a[href^="/c-SelectCategory"]').bind('click',function(){Kj.Ga.trackEventsinGA({category:'Search&Browse_PostAdLink_UpperRight',action:'Search&Browse_PostAdLink_UpperRight_clicked',opt_label:'Properties/flat+%2F+house+for+rent',track_on_area_level:true});});});$(document).ready(function(){Kj.Search.initFilter({distHlp:"Skorzystaj z wyszukiwania odległości, aby znaleźć ogłoszenia na podstawie Twojej lokalizacji i możliwości dojazdu.",srchUrl:"http://www.gumtree.pl/f-GetSearchUrl",searchFilters:{CatId:'9008',Location:'3200208',AdType:'2',Keyword:'ruczaj',maxPrice:'1 600'}});});$(document).ready(function(){Kj.Search.evenTrackingFilter({category:'LangFilter',action:"",opt_label:'Properties/flat+%2F+house+for+rent',track_on_area_level:false});});$(document).ready(function(){Kj.Search.initExpSearchGA({viewType:"-List",count:92});});$(document).ready(function(){$('#subInvite .helptip').attachHoverBubbleHelp('<div\>\r\nPowiadomienia na Gumtree to usługa powiadamiania użytkowników Gumtree poprzez e-maile o najnowszych ogłoszeniach na naszym serwisie.<br/\><br/\><a href=\"/p-EmailSubscription\" target=\"_blank\"\>Więcej pomocy</a\>\r\n</div\>');});$(document).ready(function(){Kj.Search.init();Kj.Search.initFavpanel({savedFavText:"<div\>Zachowane w <a href=\"http://www.gumtree.pl/c-SavedAds\"\>Zachowane ogłoszenia</a\></div\>",addFavText:"<div\>Kliknij, aby dodać do Zachowanych ogłoszeń</div\>"});Kj.Search.initGalleryView();});$(document).ready(function(){$('#AreaHomeTab,#SiteHomeTab').click(function(e){trackHomeTabDropdown('tabname')});$('#AreaHomeText,#SiteHomeText').addClass('browse');var freeIcon=$('#freeIcon2');if(freeIcon.length>0){freeIcon.click(function(e){document.location='c-SelectCategory';return false;});}
$('.BigSearch').attachHoverPopup('#CategoryDropdown');});Kj.initReady({});
// End-TAIL JS
</script>
<!-- customJs -->
<!-- End of HtmlPageTail -->
<div id="flashCookie"></div>
<div id="myFavorites-panel"> </div>
<script>
Kj.initFavoritesFunctionality({domain:'www.gumtree.pl',panelActivated:'true',staticsPath:'http://include.classistatic.com/include/e884/c3js/classifieds/rel1/'});
</script>
</body></html>
"""
 
OFFER1_HTML = u"""
<!DOCTYPE html PUBLIC "-//W3C//DTD OFFER_HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
 
<html xmlns="http://www.w3.org/1999/xhtml"  xmlns:fb="http://www.facebook.com/2008/fbml"> 
<head>
<title>Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego</title>
<meta http-equiv="X-UA-Compatible" content="IE=9"/>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<meta name="description" content="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego, mieszkania i domy do wynajęcia, ogłoszenia drobne na Gumtree"/>
<meta name="uniq_GUMTREE_POLAND_page_token_name" content="ViewAd"/>
<meta property="og:image" content="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_35.JPG"/>
<meta property="og:title" content="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/przytulne-2-pokojowe-35m-ruczaj-babinskiego-607878925"/>
<meta property="og:description" content="Do wynajęcia od zaraz 2-pokojowe mieszkanie przy ul. Babińskiego 23b ( I piętro). Mieszkanie ma 2 pokoje ( w tym 1 przechodni), kuchnie, łazienkę, przedpokój i balkon z widokiem. Okolica bardzo spokojna. Przystanek autobusowy &quot;Babińskiego&quot; 2 min. od "/>
<meta property="og:locality" content="Kraków"/>
<meta property="og:site_name" content="Gumtree Polska"/>
<meta property="og:country-name" content="Poland"/>
<link rel="canonical" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/przytulne-2-pokojowe-35m-ruczaj-babinskiego-607878925"/>
<link rel="SHORTCUT ICON" href="http://pic.classistatic.com/image/pics/classifieds/gumtreeFavicon.ico">
<link href="http://include.classistatic.com/include/e884/c3css/pages/ViewAdShared-min.css" rel="stylesheet" type="text/css">
<link href="http://include.classistatic.com/include/e884/c3css/brands/gumtree/PL/all-pl.css" rel="stylesheet" type="text/css">
<script type="text/javascript">
//<!--
var picsPath = "http://pic.classistatic.com/image/pics/classifieds/";
var staticPath = "http://include.classistatic.com/include/e884/c3js/classifieds/rel1/";
var debugNonProdStaticPathPrefix = "s_isProduction => true, s_localStaticPath => null, m_isSecure => false, s_localSecureStaticPath => null, nonProdStaticPathPrefix => ";
//-->
</script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/shared_pages/flashChecker.js"></script>
<script src="http://www.google.com/jsapi"></script>
<noscript>
<style type="text/css">
.jsonly {display:none;}
.collapseWithJS {display:block;}
.collapseWithJS_inline {display:inline;}
</style>
</noscript>
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['siteTracker._setAccount', 'UA-9157637-1']);
_gaq.push(['siteTracker._setDomainName', '.gumtree.pl']);
_gaq.push(['siteTracker._setSessionCookieTimeout', 1800000]);
_gaq.push(['siteTracker._setCampaignCookieTimeout', 15768000000]);
_gaq.push(['siteTracker._setVisitorCookieTimeout', 63072000000]);
_gaq.push(['siteTracker._trackPageview', '/ViewAd/properties/flat+%2f+house+for+rent/attribute']);
</script>
<script type="text/javascript">
(function() {
var ga = document.createElement("script");
ga.type = "text/javascript"; ga.async = true;
ga.src = ("https:" == document.location.protocol ? "https://ssl" : "http://www") + ".google-analytics.com/ga.js";
var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<script type="text/javascript">
var mpx_custom = {
new_mpcl: 'p;krakow;9008;Nieruchomo%C5%9Bci;l3;1;820;p;;n;607878925;http%3A%2F%2Fwww.gumtree.pl%2Fcp-mieszkania-i-domy-do-wynajecia%2Fkrakow%2Fprzytulne-2-pokojowe-35m-ruczaj-babinskiego-607878925%3FfeaturedAd%3Dtrue',
new_mpvl: document.referrer
}
</script>
</head>
<body>
<div id="main">
<div id="top">
<a name="#top"></a>
<div id="mediaplex_tracking"></div>
<script type="text/javascript">
(function() {
var mpxtag = document.createElement('script'); mpxtag.type = 'text/javascript'; mpxtag.async = true;
mpxtag.src = ('https:' == document.location.protocol
? 'https://secure.img-cdn.mediaplex.com/0/9860/56583/Kijiji-Poland_mp_pvt_brand_landing_ns_2013-04-30.js'
: 'http://img-cdn.mediaplex.com/0/9860/56583/Kijiji-Poland_mp_pvt_brand_landing_ns_2013-04-30.js');
var smpx = document.getElementsByTagName('script')[0]; smpx.parentNode.insertBefore(mpxtag, smpx);
})();
</script>
<!-- Start of HtmlPageHeader_03. This ftl is used for national site for Team 9 team -->
<script> var IsNC2_On = true; </script>
<script> var IsAdIdsSite_On = false; </script>
<table class="tbleColpse newHeader nationalSite">
<tr>
<td class="national-logo-area">
<div>
<a href="http://www.gumtree.pl" >
<img src="http://pic.classistatic.com/image/pics/classifieds/pl-PL/logo-gumtree.png" width="68" height="76" border="0" alt="Polska ">
</a>
</div> </td>
<td class="header-curve">
<div class="header-curve-top">&nbsp;</div>
<div class="header-curve-bottom">&nbsp;</div>
</td>
<td class="header-curve-space">
<div class="header-top-bg">&nbsp;</div>
<div class="header-bottom-bg">&nbsp;</div>
</td>
<td class="v-top">
<table width="100%" class="tbleColpse">
<tr>
<td class="navTabs-new h-top">
<div class="mainTabs">
<a href="http://www.gumtree.pl/c-SelectCategory" class="tabLink" >
<div id="SelectCategoryTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div> + Dodaj ogłoszenie</div>
</div></div></div>
</a>
<a href="http://www.gumtree.pl" class="tabLink" >
<div id="SiteHomeTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div id="SiteHomeText">Kategorie</div>
</div></div></div>
</a>
<a href="http://www.gumtree.pl/c-DealerDirectory" class="tabLink" >
<div id="DealerDirectoryTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div>Katalog sprzedawców</div>
</div></div></div>
</a>
</div>
</td>
<td class="lang h-top">
<div class="menuTop">
<ul>
<div id="withoutGreetings">
<li>
<!--<a href="https://secure.gumtree.pl/s-SignIn?rup=ViewAd&ruq=AdId%3D607878925" id="log_out" >here:Zaloguj się</a>-->
<span onclick="clickEncoded('aHR0cHM6Ly9zZWN1cmUuZ3VtdHJlZS5wbC9zLVNpZ25Jbj9ydXA9Vmlld0FkJnJ1cT1BZElkJTNENjA3ODc4OTI1')" class="sd-link">Zaloguj się</span>
<span class="bar">&nbsp;|&nbsp;</span>
</li>
<li>
<!--<a href="https://secure.gumtree.pl/s-StartRegistration?rup=ViewAd&ruq=AdId%3D607878925" id="log_out" >here:Zarejestruj się</a>-->
<span onclick="clickEncoded('aHR0cHM6Ly9zZWN1cmUuZ3VtdHJlZS5wbC9zLVN0YXJ0UmVnaXN0cmF0aW9uP3J1cD1WaWV3QWQmcnVxPUFkSWQlM0Q2MDc4Nzg5MjU=')" class="sd-link">Zarejestruj się</span>
<span class="bar">&nbsp;|&nbsp;</span>
</li>
<li>
<!--<a href="http://www.gumtree.pl/c-ManageMyAds" id="log_out" >here:Moje Gumtree</a>-->
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtTWFuYWdlTXlBZHM=')" class="sd-link">Moje Gumtree</span>
</li>
</div>
</ul>
</div>
</td>
</tr>
</table>
<noscript>
<style>
.msgbar{
padding-top:5px;
}
</style>
</noscript>
<table class="search-area tbleColpse header-bottom-bg">
<tr>
<td style="padding-right:10px" nowrap="true" valign="middle">
<table class="tbleColpse rel-p" width="100%" >
<tr>
<td nowrap="true" align="left">
<table class="tbleColpse">
<form action="http://www.gumtree.pl/f-SearchAdRedirect" method="get" name="frmSearchAd" id="frmSearchAd" class="searchform">
<input type="hidden" name="isSearchForm" value="true">
<tr>
<td><div class="ww_table_left"></div></td>
<td align="left" >
<table class="tbleColpse" >
<!--
<tr>
<td class="ww_table">
<div class="toplbl">here:Czego szukasz...?</div>
</td>
</tr>
-->
<tr>
<td class="ww_table" style="padding-right:10px">
<div class="flt">
<span class="left-what"></span>
<span class="keySpan lf">
<input title="Czego szukasz...?" id="autoComp" type="text" name="Keyword" value="" class="keyword center-what" autocomplete="off"/>
</span>
<span class="right-what"></span>
</div>
</td>
</tr>
</table>
</td>
<td class="ww_table" style="padding-right:10px">
<div id="searchCat" class="jsonly kjmenu_main_wrap">
<div class="left-all-cat"></div>
<div id="searchCat_name" class="center-all-cat">Wszystkie kategorie<img border="0" src="http://pic.classistatic.com/image/pics/classifieds/spacer.gif" width="25px" height="1px"/></div>
<div class="button-arrow"></div>
</div>
<input class="jsonly" type="hidden" name="CatId" value="0"/>
</td>
<td class="ww_table">
<div id="searchLoc" class="jsonly kjmenu_main_wrap">
<div class="left-all-cat"></div>
<div id="searchLoc_name" class="center-all-cat">Kraków<img border="0" src="http://pic.classistatic.com/image/pics/classifieds/spacer.gif" width="25px" height="1px"/></div>
<div class="button-arrow"></div>
</div>
<input class="jsonly" type="hidden" name="Location" value=""/>
</td>
<td class="ww_table" style="padding-left:10px">
<span class="left-search"></span>
<input id="searchAdGo" type="submit" value="Szukaj" class="searchButton" />
<span class="right-search"></span>
</td>
<td><div class="ww_table_right"></div></td>
</tr>
</form>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<div id="CategoryDropdown" class="popupWindow">
<ul class="catlistdropdown">
<li class="item">
<span class="cursptr" id="catId0" onClick="swapCat(this,'0');">Wszystkie ogłoszenia</span>
</li>
<li class="item">
<span class="cursptr" id="catId2" onClick="swapCat(this,'2');">Nieruchomości</span>
</li>
<li class="item">
<span class="cursptr" id="catId4" onClick="swapCat(this,'4');">Sprzedam</span>
</li>
<li class="item">
<span class="cursptr" id="catId8" onClick="swapCat(this,'8');">Oferty Pracy</span>
</li>
<li class="item">
<span class="cursptr" id="catId5" onClick="swapCat(this,'5');">Motoryzacja</span>
</li>
<li class="item">
<span class="cursptr" id="catId9290" onClick="swapCat(this,'9290');">Szukający Zatrudnienia</span>
</li>
<li class="item">
<span class="cursptr" id="catId9541" onClick="swapCat(this,'9541');">Moda</span>
</li>
<li class="item">
<span class="cursptr" id="catId9218" onClick="swapCat(this,'9218');">Łodzie i Pojazdy wodne</span>
</li>
<li class="item">
<span class="cursptr" id="catId9237" onClick="swapCat(this,'9237');">Elektronika</span>
</li>
<li class="item">
<span class="cursptr" id="catId9" onClick="swapCat(this,'9');">Usługi</span>
</li>
<li class="item">
<span class="cursptr" id="catId9459" onClick="swapCat(this,'9459');">Dla Dziecka</span>
</li>
<li class="item">
<span class="cursptr" id="catId9124" onClick="swapCat(this,'9124');">Zwierzaki</span>
</li>
<li class="item">
<span class="cursptr" id="catId9490" onClick="swapCat(this,'9490');">Sport i Rozrywka</span>
</li>
<li class="item">
<span class="cursptr" id="catId6" onClick="swapCat(this,'6');">Społeczność</span>
</li>
</ul>
</div>
<div class=popWords>
<div class="floatLeft30px">
Popularne
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/radzikowskiego/c9008" title="radzikowskiego">radzikowskiego</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/wieczysta/c9008" title="wieczysta">wieczysta</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/radzymin/c9008" title="radzymin">radzymin</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/strzeszyn/c9008" title="strzeszyn">strzeszyn</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/saska/c9008" title="saska">saska</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/jab%C5%82onna/c9008" title="jabłonna">jabłonna</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/sosnowiec/c9008" title="sosnowiec">sosnowiec</a>
</div>
</div>
<div class="greyBottom300">
</div>
<div id="pagestatus_new" style="">
</div>
</div>
<div id="middle" class="page_viewad">
<div class="VAStyleA">
<div id="viewad_header">
<table class="tbleColpse viewadhdr">
<tr>
<td valign="top">
<div id="breadcrumbVIP">
<div itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
<a href="http://www.gumtree.pl" itemprop="url">
<span itemprop="title">Polska</span>
</a> &gt; <a href="http://www.gumtree.pl/fp-nieruchomosci/krakow/c2l3200208" itemprop="url">
<span itemprop="title">Nieruchomości</span>
</a>
>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/c9008l3200208" itemprop="url">
<span itemprop="title">mieszkania i domy do wynajęcia</span>
</a>
&gt; Nr referencyjny ogłoszenia 607878925
</div>
</div>
<div><div id='div-gpt-ad-1363883804543-leader' style="margin:0 auto;text-align:center;">
</div>
<div id='div-gpt-ad-vip-topbanner' style='text-align:center;margin:0px auto'></div></div>
</td>
<td align="right" valign="top">
</td>
</tr>
</table>
<table class="viewadtitle">
<tr>
<td class="viewadtitleL viewadtitleLComm">
<table class="tbleColpse">
<tr>
<td >
<div >
<h1 class="" id="preview-local-title" >
<!-- google_ad_section_start -->Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego<!-- google_ad_section_end -->
</h1>
</div>
</td>
</tr>
</table>
</td>
<td class="viewadaction">
<ul id="viewAd-actions" class="viewAd-actions" >
<li><span nowrap="true" class="jsonly wl_star_off" title="Zachowaj ogłoszenie">&nbsp;&nbsp;&nbsp;&nbsp;<span class="watchText">Zachowaj</span></span></li>
<li class="pipe">|</li>
<li>
<span class="s2f">
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtU2VuZFRvRnJpZW5kP0FkSWQ9NjA3ODc4OTI1')" class="sudo-link">Udostępnij</span>
</span>
</li>
<li class="pipe">|</li>
<li>
<!-- rt:5001 - Removing icon labels if Print has empty content in ViewAd.xml-->
<span class="print">
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtUHJpbnRBZD9BZElkPTYwNzg3ODkyNQ==', '_blank')" class="sudo-link">Drukuj</span>
</span>
</li>
<li class="pipe">|</li>
<li> <span class="jsonly" id="reportAd_name">Zgłoś ogłoszenie<span>&nbsp;&nbsp;&nbsp;</span></span>
<div class="modal" id="modalFrameLayer"></div>
</li>
</ul>
</td>
</tr>
</table>
</div>
<noscript>
<style type="text/css">
.jsonly {
display:none;
}
</style>
</noscript>
<table class="adcontent tblClpsePad">
<tr>
<td>
<table width="100%" class="tblClpsePad"
>
<tr>
<td class="adImg">
<div style="margin-bottom:5px;">
<table cellpadding="0" cellspacing="0" border="0" class="viewad_images viewad_frame_tbl" >
<tr>
<td class="viewad_images viewad_frame_fill">
<table width="100%" height="3" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=bottom class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_tl viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_images viewad_frame_tm viewad_images viewad_frame_brand1" style="font-size:3px">
<div class="viewad_images viewad_frame_fill"> </div>
</td>
<td valign=bottom class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_tr viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td class="viewad_images viewad_frame_m viewad_images viewad_frame_brand2" style="margin:0px">
<table width="100%" class="gallery viewad_frame_brand2 tbleColpse viewadimgcontr">
<tr>
<td align=middle class="imageStack " imggal='main'>
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtVmlld0FkTGFyZ2VJbWFnZT9BZElkPTYwNzg3ODkyNSZLZXl3b3JkPWtyYWtvdw==')" class="sudo-link" title='Zoom'>
<img class="view" title="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego" alt="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego image0" src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_35.JPG" border="0" />
</span>
</td>
</tr>
</table>
<center>
<table class="img-next-prev tbleColpse">
<tr>
<td class="jsonly">
<div class="prev" imggal='prev'>&nbsp; </div>
</td>
<td style="padding:0px 10px 0px 10px">
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtVmlld0FkTGFyZ2VJbWFnZT9BZElkPTYwNzg3ODkyNSZLZXl3b3JkPWtyYWtvdw==')" class="sudo-link" title='Zoom' imggal='viewimg'>
<div class="view-large">
<div> Powiększ obraz </div>
</div>
</span>
</td>
<td class="jsonly">
<div class="next" imggal='next'>&nbsp; </div>
</td>
</tr>
</table>
</center>
<table class='navs' cellpadding="0" cellspacing="0" border="0">
<tr class="imageNavs">
</tr>
<tr class="imageNavs">
<td imggal="thumb" imgindx="0" class="ni active">
<img src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="1" class="ni">
<img src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/gacAAOSwxCxT195J/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="2" class="ni">
<img src="http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/Tu0AAOSwPe1T195v/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="3" class="ni">
<img src="http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/EbQAAOSw7NNT1956/$_14.JPG" border="0"/>
</td>
</tr>
<tr class="imageNavs">
<td imggal="thumb" imgindx="4" class="ni">
<img src="http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/lKUAAOSwRLZT196P/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="5" class="ni">
<img src="http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/a78AAOSwEK9T196h/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="6" class="ni">
<img src="http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/bj4AAOSwEK9T1963/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="7" class="ni">
<img src="http://i.ebayimg.com/00/s/MTAwMFg3NTA=/z/JKUAAOSwQItT197E/$_14.JPG" border="0"/>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td class="viewad_images viewad_frame_fill">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=top class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_bl viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_images viewad_frame_bm viewad_images viewad_frame_brand1" style="font-size:3px;height:3px">
<div class="viewad_images viewad_frame_fill"> </div>
</td>
<td valign=top class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_br viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</div>
</td>
<td valign="top" width="99%">
<div style="font-weight:normal">
<table cellpadding="0" cellspacing="0" border="0" class="viewad_frame_tbl" style="min-width:260px;">
<tr>
<td class="viewad_frame_fill">
<table width="100%" height="3" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=bottom class="viewad_frame_fill">
<div class="viewad_frame_tl viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_frame_tm viewad_frame_brand1" style="font-size:3px">
<div class="viewad_frame_fill"> </div>
</td>
<td valign=bottom class="viewad_frame_fill">
<div class="viewad_frame_tr viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td class="viewad_frame_m viewad_frame_brand2" style='padding:0px 2px 0px 2px' style="margin:0px"> <table id="attributeTable" border="0" cellpadding="3" cellspacing="0" width="100%">
<col/><col width="99%"/>
<tbody>
<tr>
<td nowrap valign=top class="first_col first_row " >Data dodania
</td>
<td class="first_row" > 29/07/2014
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Cena
</td>
<td style='font-weight:bold'> Zł  950,00
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Adres
</td>
<td itemscope itemtype="http://schema.org/Place"> Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska
<br>
<span class="viewmap-link sudo-link">Pokaż mapę</span>
</td>
</tr> <div id="viewmap-modal" style="display:none"> <div id="gmap" style="width:100%; height:507px" valign="top">
<noscript>
<strong>Adres:</strong> Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska<br>
</noscript>
</div>
</div>
<tr>
<td nowrap valign=top class="first_col " >Do wynajęcia przez
</td>
<td > Właściciel
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Rodzaj nieruchomości
</td>
<td > Mieszkanie
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Liczba pokoi
</td>
<td > 2 pokoje
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Wielkość (m2)
</td>
<td > 36
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Liczba łazienek
</td>
<td > 1 łazienka
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Parking
</td>
<td > Ulica
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Przyjazne zwierzakom
</td>
<td > Tak
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="viewad_frame_fill">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=top class="viewad_frame_fill">
<div class="viewad_frame_bl viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_frame_bm viewad_frame_brand1" style="font-size:3px;height:3px">
<div class="viewad_frame_fill"> </div>
</td>
<td valign=top class="viewad_frame_fill">
<div class="viewad_frame_br viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
</table>
<div id="ad-desc" class="ad-desc" class="marginTop10px" >
<!-- google_ad_section_start -->
<span id="preview-local-desc">
Do wynajęcia od zaraz 2-pokojowe mieszkanie przy ul. Babińskiego 23b ( I piętro). Mieszkanie ma 2 pokoje ( w tym 1 przechodni), kuchnie, łazienkę, przedpokój i balkon z widokiem. Okolica bardzo spokojna. Przystanek autobusowy "Babińskiego" 2 min. od bloku, przystanek "Zachodnia" 7 min. Dojazd do centrum zajmuje ok. 30 min. Do miasta można również dojeżdżać busikami jeżdżącymi ze Skawiny, jest się wówczas w okolicach centrum( busiki jeżdżą pod Dworzec lub pod Pocztę Główną) w ok. 20 min.<br/>Przed blokiem jest miejsce do parkowania. Z balkonu ładny widok, żadnych bloków na horyzoncie:) Mieszkanie przytulne, remontowane kilka lat temu. Mieszkanie w pełni wyposażone (pralka, lodówka, kuchenka, piekarnik). Nowe okna, ogrzewanie miejskie. Opłaty miesięczne to ok. 450 zł przy 2 osobach (czynsz administracyjny + prąd).
</span>
<!-- google_ad_section_end -->
</div>
<div class="cenvis">
<span class="visits">Wizyty: 383 </span>
</div>
</div>
</td>
</tr>
<tr>
</tr>
</table>
<br/>
<style>
.page_viewad #viewAd-actions .s2f, #viewad_header #viewAd-actions .s2f { background-image: url("http://pic.classistatic.com/image/site/ca/icons/facebook.gif"); }
.stack-adsense-title { background-color: #fdeb6b; } .weburl { text-overflow:ellipsis; overflow: hidden; white-space: nowrap; width: 260px } .right_logo_box.brand_border { text-align: center; height: auto; }
.viewAdImgTitle { height: auto; }
</style>
<div class="similarads clearfix">
<div class="titlebar">
Podobne ogłoszenia
</div>
<div class="maindiv">
<div class="contentdiv">
<div class="imagediv">
<a id="sa606759499" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ekskluzywny-apartament-3-pokoje-75m2-obok-dworca-okazja-606759499">
<img src="http://i.ebayimg.com/00/s/ODAyWDEwMjQ=/z/N6cAAOSw9NxTvmZu/$_14.JPG" border="0" />
</a>
</div>
<a id="sa606759499" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ekskluzywny-apartament-3-pokoje-75m2-obok-dworca-okazja-606759499">
<div class="pricediv">
Zł  3 000,00
</div>
<div class="titlediv">
Ekskluzywny apartament 3-pokoje, 75m2, obok dworca OKAZJA
</div>
<div class="datediv">
Dodane: 10/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607359596" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/plac-matejki-stary-kleparz-kawalerka-sw-filipa-607359596">
<img src="http://i.ebayimg.com/00/s/MTAwMFg2Njc=/z/89YAAOSwKPNTzCvI/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607359596" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/plac-matejki-stary-kleparz-kawalerka-sw-filipa-607359596">
<div class="pricediv">
Zł  1 100,00
</div>
<div class="titlediv">
PLAC MATEJKI, STARY KLEPARZ, kawalerka, Św. Filipa
</div>
<div class="datediv">
Dodane: 20/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607937278" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/nowoczesne-apartament-75m2-ul-bronowicka-2600pln-607937278">
<img src="http://i.ebayimg.com/00/s/NDI2WDY0MA==/z/b~IAAOSwVFlT2SZr/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607937278" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/nowoczesne-apartament-75m2-ul-bronowicka-2600pln-607937278">
<div class="pricediv">
Zł  2 600,00
</div>
<div class="titlediv">
Nowoczesne apartament 75m2,ul.Bronowicka 2600pln
</div>
<div class="datediv">
Dodane: 30/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607315619" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/super-lokalizacja-ul-grzegorzecka-jeden-pokoj-607315619">
<img src="http://i.ebayimg.com/00/s/NDMyWDY0MA==/z/PxEAAOSwq7JTyrb2/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607315619" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/super-lokalizacja-ul-grzegorzecka-jeden-pokoj-607315619">
<div class="pricediv">
Zł  1 350,00
</div>
<div class="titlediv">
Super lokalizacja, ul. Grzegórzecka, jeden pokój
</div>
<div class="datediv">
Dodane: 19/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607888553" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-krakow-krowodrza-25m2-nr-9848-607888553">
<img src="http://i.ebayimg.com/00/s/NDIyWDY0MA==/z/RfsAAOSwVFlT2Edv/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607888553" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-krakow-krowodrza-25m2-nr-9848-607888553">
<div class="pricediv">
Zł  1 000,00
</div>
<div class="titlediv">
Mieszkanie Kraków Krowodrza 25m2 (nr: 9848)
</div>
<div class="datediv">
Dodane: 30/07/2014
</div>
</a>
</div>
</div>
</div>
</div>
<br/>
<div id="googsense"></div>
</td>
<td class="viewadrightcol" style="margin:0px;padding:0px 0px 0px 15px">
<div class="alternate-box">
<div class="alternate-contact-info">DANE KONTAKTOWE</div>
<div class="alternate-phone-box">
<div class="alternate-phone-icon">&nbsp;</div>
<div id="phn-text">
<span class="alternate-phone-number">796...</span>
<div class="alternate-show-phone-bar">
<span class="alt-ph-hover"><span class="alternate-show-phone-bar-left">&nbsp;</span><span class="alternate-show-phone-bar-center"><a class="alternate-show-phone-number" href="javascript:">Pokaż numer telefonu</a></span><span class="alternate-show-phone-bar-right">&nbsp;</span></span>
</div>
</div>
</div>
<div id='phoneclicktracking'></div>
<noscript>
<div style="padding-bottom:5px;">
<div class='PhoneIcon' style="padding-left:20px"><img src="http://ext.classistatic.com/imagesvc/txt2Img/GUEZdyU-ESoSSRTaZ2_migZN4p6ySNa6tvalAmTk8edZ_tEvl1pIsw0YiCmruWY7lfOS2C9fMOrYlqYYRLYuxlqlNZxEKQ3z3L3xROIA6g9VkYpUgu8BCpbDtF9G3dtl697ZG_0GJzgYQ8lfczz8grOcLGgqeZM5lmO6v_2TQ0kpivdwLq4RALJ0PcV45o6zjKe2rHWMA6IXrG9ukmK0xJeQ03Tyg_0iAwuL9yw9Rx8" style="border:none;" /> </div>
</div>
</noscript> <div class="alternate-email-label">Skontaktuj się przez e-mail</div>
<div class="email_block brand_border">
<div id="viewad_email">
<form id="ReplyToAdForm" action="/c-ViewAd" method="post" name="viewadfrm">
<noscript>
<style type="text/css">
#ReplyToAdForm .first-input div {
padding-left : 0px;
background : transparent;
}
</style>
</noscript>
<input type="hidden" name="AdId" value="607878925"/>
<input type="hidden" name="Submit" value="true"/>
<span id="MTNew" >
</span>
<span id="CDOld" >
<div id="SenderEmailAddress_field" class="first-field" >
<div class="first-input">
<a name="FromEmailAddress"></a>
<div class="input-div">
<input type="text" name="FromEmailAddress" value=""
id="SenderEmailAddress"
title="Twój e-mail"
style="width:100%"
class="reply-field"
size="30"
/>
</div>
</div>
</div>
</span>
<span id="MTOld" >
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblEmailText" ><noscript>Wiadomość</noscript></span>
</div>
<div class="first-input">
<a name="EmailText"></a>
<div class="input-div">
<textarea name="EmailText"
cols="25"
title="Wiadomość"
style="width:290px; margin-top:7px;"
class="reply-field"
rows="4"
></textarea>
</div>
</div>
</div>
</span>
<span id="CDNew">
</span>
<div class="alternate-checkbox">
<input type="checkbox" name="CopyMe" value="checked" checked/> Wyślij mi kopię e-maila
</div>
<div class="alternate-submit-box">
<span class="alternate-submit-left">&nbsp;</span><input type="submit" id="send" value='WYŚLIJ E-MAIL' class="alternate-submit-center"/><span class="alternate-submit-right">&nbsp;</span>
<div style="clear:both;"></div>
</div>
</form>
<div class="alternate-help-text">
Klikając „Wyślij”, wyrażasz zgodę na nasze <span onclick="clickEncoded('L3AtVGVybXNBbmRDb25kaXRpb25z')" class="sudo-link" >Zasady korzystania</span> i <span onclick="clickEncoded('L3AtUHJpdmFjeQ==')" class="sudo-link" >Politykę prywatności</span>. Twoja wiadomość zostanie wysłana do ogłoszeniodawcy i nie będzie widoczna publicznie.
</div>
</div>
</div>
<div class="alternate-line">&nbsp;</div>
<div class="alternate-posted-by-box">
<div class="alternate-view-all-ads"> <span class="alternate-active-since">
Aktywny od: lip 2014
</span>
</div>
<div class="alternate-top-p2">&nbsp;</div>
<div class="alternate-icon-poster ">&nbsp;</div>
<div class="alternate-poster-info"> <span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtUG9zdGVyc090aGVyQWRzLVcwUVFVc2VySWRaOTM0NjE5NzE=')" class="sudo-link"> Zobacz wszystkie ogłoszenia tego użytkownika Gumtree
</span>
</div>
<div>&nbsp;</div>
</div>
</div>
<div><p>
<center>
<script jsinline type="text/javascript">
mpt = new Date();
mpts = mpt.getTimezoneOffset() + mpt.getTime();
if (!document.layers) {
document.writeln("<scr"+"ipt type=\"text\/javascript\" src=\"http:\/\/altfarm.mediaplex.com\/ad\/js\/10832-110408-23165-0\?mpt=" + mpts + "&mpvc=\"><\/script>");
} else {
document.write("<a href=\"http://altfarm.mediaplex.com/ad/ck/10832-110408-23165-0?mpt=" + mpts + "\"><img src=\"http://altfarm.mediaplex.com/ad/bn/10832-110408-23165-0?mpt=" + mpts
+ "\" alt=\"Click Here\" border=\"0\"></a>" );
}
</script>
<noscript>
<a href="http://altfarm.mediaplex.com/ad/nc/10832-110408-23165-0">
<img src="http://altfarm.mediaplex.com/ad/nb/10832-110408-23165-0"
alt="Click Here" border="0">
</a>
</noscript>
</center>
<p>
<!-- Ad section -->
<div id='div-gpt-ad-1318934199048-0' style='width:300px; height:250px;margin:6px auto'></div>
<div id='div-gpt-ad-1318934199048-1' style='width:300px; height:250px;margin:6px auto'></div></div>
<br/>
<br/>
</td>
</tr>
</table>
</div>
</div>
<div id="bottom">
<div class="footer">
<div>
<link type="text/css" rel="stylesheet" href="https://securepic.classistatic.com/image/site/au/global_footer/new_global_footer.css" />
<style type="text/css">
.footer {
border-top: 0px solid #BEC3C7;
margin: 0px 0px 0px 15px;
padding: 10px 0 10px 0;
}
.footer li {
list-style:none;
display: list-item;
color: #676B5C;
font-size:11px;
margin:0;
padding:0 5px 0 0;
border-right: 0px solid #ffffcc;
}
.get-to-know-us,.explore-gumtree,.legalbits,.tips-help,.blog-latest,.gumtree-elsewhere{
display:inline;
float:left;
}
.get-to-know-us{
margin-left:10px;
}
.blog-latest{
margin-left:0px;
}
#footer-links > div {
margin-right: 10px;
width: 150px;
}
#footer-links .gumtree-elsewhere {
width: 120px;
}
#footer .social-facebook,
#footer .social-twitter,
#footer .social-google,
#footer .social-pinterest,
#footer .social-youtube{ display:block; margin-bottom:3px; height:18px; line-height:18px; padding-left:20px; background-repeat:no-repeat; background-position:left center; background-size:18px 18px; }
</style>
<div id="footer" class="footer">
<div id="footer-links" class="container">
<div class="gumtree-legal" style="display:inline">
<h3><a href="http://www.gumtree.pl">
<img src="http://pic.classistatic.com/image/site/au/global_footer/footer_logo.gif" border="0" alt=""></a></h3>
</div>
<div class="get-to-know-us">
<h3>Poznaj nas</h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=122">O Gumtree</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?category=5">Zasady zamieszczania ogłoszeń</a></li>
</ul>
</div>
<div class="explore-gumtree">
<h3>Odkryj więcej</h3>
<ul>
<li><a href="http://info.gumtree.pl/promowanie/index.html">Promowanie ogłoszeń</a></li>
<li><a href="http://www.gumtree.pl/c-PopularSearches">Popularne wyszukiwania</a></li>
</ul>
</div>
<div class="legalbits">
<h3>Sprawy prawne</h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=120">Zasady korzystania</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=121">Polityka Prywatności</a></li>
</ul>
</div>
<div class="tips-help">
<h3>Pomoc i porady </h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php">Pomoc</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?category=7">Pozostań bezpiecznym </a></li>
<li><a href="http://gumtreehelp.com/pl/index.php">Napisz do nas </a></li>
<li><a href="http://blog.gumtree.pl/">Gumtree Blog </a></li>
</ul>
</div>
<div class="gumtree-elsewhere">
<h3>Śledź nas</h3>
<ul>
<li><a class="social-facebook" href="https://www.facebook.com/GumtreePolska" target="_blank">Facebook</a></li>
<li><a class="social-google" href="https://plus.google.com/103950977256553454134/posts" rel="publisher" target="_blank">Google+</a></li>
<li><a class="social-twitter" href="https://twitter.com/gumtreepolska" target="_blank">Twitter</a></li>
<li><a class="social-youtube" href="http://www.youtube.com/user/GumtreePolska" target="_blank">YouTube</a></li>
<li><a class="social-pinterest" href="http://pinterest.com/gumtreepolska" target="_blank">Pinterest</a></li>
</ul>
</div>
<div class="blog-latest">
</div>
</div>
<!-- Start Alexa Certify Javascript -->
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=wS4fj1a4ZP00g+" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
<div id="copyright">&nbsp;</div>
</div>
<div class="cpyrt">
Copyright © 2014 eBay International AG
</div>
<!--<style> html .fb_share_link { margin-left: 5px; padding:0 0 0 20px; height:16px; background:url(http://b.static.ak.fbcdn.net/images/share/facebook_share_icon.gif?8:26981) no-repeat top left; }</style>
<a href="http://altfarm.mediaplex.com/ad/ck/9860-90999-23165-0?mpt=1&mpre=http%3A//www.facebook.com/share.php%3Fu%3Dhttp%3A//gumtree.pl.gumtree.pl/c-ViewAd%3FAdId%3D607878925" onclick="return fbs_click()" target="_blank" class="fb_share_link"><font size="2">Dołącz do Fanów na Facebook'u</font></a>&nbsp;&nbsp;|<img src="http://pic.classistatic.com/image/site/au/twitter_16x16_FFFAEE.GIF" hspace="5"/><a href="http://twitter.com/gumtreepolska/" target="_blank"><font size="2">Śledź nas na Twitterze</font></a>-->
</div>
</div>
</div>
<!-- Start of HtmlPageTail -->
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/common/common-min.js"></script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1//pages/viewAd-min.js"></script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/shared_pages/mapServices-min.js"></script>
<div id="OandN" class="modal">
<table cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="modalHeading">
<div class="layerTitleText"></div>
<div class="closeBtn close" title="Close">&nbsp;</div>
</td>
</tr>
<tr class="layerContent">
<td>
<div id="OandNContent" class="OandNCont">
<div class="OandNData">
<b>Oferty:</b> Ogłoszenia z ceną mogą zawierać również opcję złożenia oferty. Złożone oferty nie są wiążące. Ogłoszeniodawca otrzymuje szczegóły oferty po jej złożeniu. Ogłoszeniodawca może odpowiedzieć na ofertę lub nie.
<br/><br/></br>
<b>Powiadomienia:</b> Podczas składania oferty możesz zdecydować się na codzienne powiadomienia, jeśli dla ogłoszenia złożono więcej ofert. Możesz zdecydować o nieprzyjmowaniu tych powiadomień poprzez usunięcie zaznaczenia z pola wyboru.
</div>
</div>
</td>
</tr>
</table>
</div>
<script>
var kj_ads_queryParam = {"adsenseQuery":"Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego","afsChannels":"r_Krakow,Total,c_housing,l_vip","locale":"pl-PL","adsenseClientAFS":"gumtree-pl-vip","type":"google","afcChannels":"r_Krakow,Total,c_housing","pageNum":"1","totalAds":3,"isGoogleTest":false,"adSafe":false,"adsenseClientAFC":"","invocationType":"afs","afcClientId":"ca-gumtree-pl_js"};
var kj_ads_dispParam = {"layOut":"","mediaplexDomain":"http://mktg.gumtree.pl/cm/bk/","dispType":"vip","trackType":"mplx","mplxUrl":"9860-56167-3840-27?LocClass-AdSenseClick=1&amp;mpuid=;;;;;;;r_Krakow,c_housing;;1406784571895"};
kj_ads_dispParam.imgPlaceHolderIconUrl = 'http://pic.classistatic.com/image/pics/classifieds/pl-PL/image_placeholder_gt1.gif';
kj_ads_dispParam.adSenseTitle = 'Linki sponsorowane';
</script>
<script>
Kj_ad.init(kj_ads_queryParam,kj_ads_dispParam);
</script>
<style>
#persistInput.storeMachId {behavior:url(#default#userData);}
</style>
<form id="persistForm">
<input type="hidden" class="storeMachId" id="persistInput"/>
</form>
<script>
Kj.initMachineId({isProduction:true,cookiePath:'http://include.classistatic.com/include/e884/c3js/classifieds/rel1/FLASH/'});
</script>
<!-- CC JS Includes -->
<script type="text/javascript" charset="UTF-8">
//start-CC JS
$().ready(function(){$(".s2f").kjmenu_makeMenu({data:"\0030\003Podziel się na Facebooku\0030\004"+"\0031\003Podziel się na Twitterze\0031\004"+"\0033\003Wyślij znajomym\0033",OnSelect:function(mitem){switch(mitem.value){case'0':window.open('http://www.facebook.com/share.php?src=bm&u=http%3A%2F%2Fgumtree.pl%2Fc-ViewAd%3FAdId%3D607878925%26utm_source%3DFacebook%26utm_medium%3DSocial%252BMedia%26utm_campaign%3DPost%252BTo%252BFacebook&t=Przytulne%2C%202%20pokojowe%2C%2035m%2C%20Ruczaj%2C%20Babi%C5%84skiego%20-%20Gumtree%20Polska&v=3');break;case'1':window.open('http://twitter.com/?status=http%3A%2F%2Fgumtree.pl%2Fc-ViewAd%3FAdId%3D607878925');break;case'3':location.href='/c-SendToFriend?AdId=607878925';break;}}});});var googletag=googletag||{};googletag.cmd=googletag.cmd||[];(function(){var gads=document.createElement('script');gads.async=true;gads.type='text/javascript';var useSSL='https:'==document.location.protocol;gads.src=(useSSL?'https:':'http:')+'//www.googletagservices.com/tag/js/gpt.js';var node=document.getElementsByTagName('script')[0];node.parentNode.insertBefore(gads,node);})();$(document).ready(function(){pageURL=window.location.href;curLOC=$("#searchLoc_name").text()||"";curLOC=curLOC.replace(/\W+/g,'_');googletag.cmd.push(function(){googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci_VIP/mieszkania_i_domy_do_wynaj_cia',[300,250],'div-gpt-ad-1318934199048-0').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","Przytulne,2,pokojowe,35m,Ruczaj,Babi,skiego").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci_VIP/mieszkania_i_domy_do_wynaj_cia',[300,250],'div-gpt-ad-1318934199048-1').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","Przytulne,2,pokojowe,35m,Ruczaj,Babi,skiego").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci_VIP/mieszkania_i_domy_do_wynaj_cia',[[728,90],[750,200]],'div-gpt-ad-vip-topbanner').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","Przytulne,2,pokojowe,35m,Ruczaj,Babi,skiego").setTargeting("dc_ref",pageURL);googletag.enableServices();});googletag.cmd.push(function(){googletag.display('div-gpt-ad-1318934199048-0');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-1318934199048-1');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-vip-topbanner');});});setTimeout(function(){var a=document.createElement("script");var b=document.getElementsByTagName("script")[0];a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0017/0492.js?"+Math.floor(new Date().getTime()/3600000);a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)},1);_atrk_opts={atrk_acct:"wS4fj1a4ZP00g+",domain:"gumtree.pl",dynamic:true};(function(){var as=document.createElement('script');as.type='text/javascript';as.async=true;as.src="https://d31qbv1cthcecs.cloudfront.net/atrk.js";var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as,s);})();
//end -CC JS
//start-TAIL JS
Kj.initGA({isGaSiteTrackerId:true,isGaTrackerId:false});$(document).ready(function(){$('.mainTabs a[href$="c-SelectCategory"]').bind('click',function(){Kj.Ga.trackEventsinGA({category:'Header_PostAdTab',action:'Header_PostAdTab_clicked',opt_label:undefined,track_on_area_level:true});});});var catdata="\0030\003Wszystkie kategorie\0030\0031\0030\004\0030-0\003Nieruchomości\0032\0031\0031\0040-0\0030-0_0\003Wszystkie Nieruchomości\0032\0031\0030\0040-0\0030-0_1\003pokoje do wynajęcia\0039000\0031\0031\0040-0\0030-0_2\003mieszkania i domy do wynajęcia\0039008\0031\0031\0040-0\0030-0_3\003mieszkania i domy - sprzedam i kupię\0039073\0031\0031\0040-0\0030-0_4\003działki\0039194\0031\0031\0040-0\0030-0_5\003krótki termin i noclegi\0039074\0031\0031\0040-0\0030-0_6\003kwatery i domki letniskowe\0039193\0031\0031\0040-0\0030-0_7\003lokal i biuro\0039072\0031\0031\0040-0\0030-0_8\003parking i garaż\0039071\0031\0031\004\0030-1\003Motoryzacja\0035\0031\0031\0040-1\0030-1_0\003Wszystkie Motoryzacja\0035\0031\0030\0040-1\0030-1_1\003samochody osobowe\0039026\0031\0031\0040-1\0030-1_2\003samochody dostawcze\0039027\0031\0031\0040-1\0030-1_3\003motocykle i skutery\0039028\0031\0031\0040-1\0030-1_4\003ciągniki i maszyny rolnicze\0039154\0031\0031\0040-1\0030-1_5\003przyczepy i naczepy\0039155\0031\0031\0040-1\0030-1_6\003części i akcesoria\0039029\0031\0031\004\0030-2\003Łodzie i Pojazdy wodne\0039218\0031\0031\0040-2\0030-2_0\003Wszystkie Łodzie i Pojazdy wodne\0039218\0031\0030\0040-2\0030-2_1\003motorówki\0039219\0031\0031\0040-2\0030-2_2\003skutery wodne\0039222\0031\0031\0040-2\0030-2_3\003żaglówki\0039221\0031\0031\0040-2\0030-2_4\003kajaki i pontony\0039220\0031\0031\0040-2\0030-2_5\003silniki do łodzi\0039223\0031\0031\0040-2\0030-2_6\003akcesoria do łodzi\0039224\0031\0031\0040-2\0030-2_7\003inne pojazdy wodne\0039225\0031\0031\0040-2\0030-2_8\003łodzie wiosłowe\0039226\0031\0031\004\0030-3\003Sprzedam\0034\0031\0031\0040-3\0030-3_0\003Wszystkie Sprzedam\0034\0031\0030\0040-3\0030-3_1\003AGD\0039366\0031\0031\0040-3\0030-3_2\003antyki i kolekcje\0039351\0031\0031\0040-3\0030-3_3\003meble\0039376\0031\0031\0040-3\0030-3_4\003narzędzia i materiały budowlane\0039384\0031\0031\0040-3\0030-3_5\003ogród\0039398\0031\0031\0040-3\0030-3_6\003produkty żywnościowe\0039407\0031\0031\0040-3\0030-3_7\003wyposażenie wnętrz\0039408\0031\0031\0040-3\0030-3_8\003zdrowie\0039418\0031\0031\0040-3\0030-3_9\003sprzedam inne\0039023\0031\0031\004\0030-4\003Elektronika\0039237\0031\0031\0040-4\0030-4_0\003Wszystkie Elektronika\0039237\0031\0030\0040-4\0030-4_1\003audio i hi-fi\0039260\0031\0031\0040-4\0030-4_2\003cesje\0039353\0031\0031\0040-4\0030-4_3\003fotografia i video\0039281\0031\0031\0040-4\0030-4_4\003gry video i konsole\0039265\0031\0031\0040-4\0030-4_5\003komputery i software\0039238\0031\0031\0040-4\0030-4_6\003radiokomunikacja\0039352\0031\0031\0040-4\0030-4_7\003tablety i bookreadery\0039259\0031\0031\0040-4\0030-4_8\003telefony i akcesoria\0039247\0031\0031\0040-4\0030-4_9\003telewizory i odtwarzacze\0039276\0031\0031\0040-4\0030-4_10\003elektronika inne\0039286\0031\0031\004\0030-5\003Dla Dziecka\0039459\0031\0031\0040-5\0030-5_0\003Wszystkie Dla Dziecka\0039459\0031\0030\0040-5\0030-5_1\003artykuły szkolne\0039468\0031\0031\0040-5\0030-5_2\003bezpieczeństwo i zdrowie dziecka\0039460\0031\0031\0040-5\0030-5_3\003buty dla dzieci\0039461\0031\0031\0040-5\0030-5_4\003chrzciny, komunie, imprezy\0039469\0031\0031\0040-5\0030-5_5\003ciąża i karmienie\0039464\0031\0031\0040-5\0030-5_6\003foteliki - nosidełka\0039462\0031\0031\0040-5\0030-5_7\003kąpiel i zdrowie\0039470\0031\0031\0040-5\0030-5_8\003kojce i chodziki\0039471\0031\0031\0040-5\0030-5_9\003meble i wystrój pokoju\0039463\0031\0031\0040-5\0030-5_10\003rowerki i inne pojazdy\0039472\0031\0031\0040-5\0030-5_11\003odzież dziecięca\0039465\0031\0031\0040-5\0030-5_12\003wózki dla dzieci\0039466\0031\0031\0040-5\0030-5_13\003zabawki\0039467\0031\0031\0040-5\0030-5_14\003inne dla dziecka\0039489\0031\0031\004\0030-6\003Sport i Rozrywka\0039490\0031\0031\0040-6\0030-6_0\003Wszystkie Sport i Rozrywka\0039490\0031\0030\0040-6\0030-6_1\003bilety\0039491\0031\0031\0040-6\0030-6_2\003instrumenty i akcesoria muzyczne\0039496\0031\0031\0040-6\0030-6_3\003komiksy i czasopisma\0039497\0031\0031\0040-6\0030-6_4\003książki\0039498\0031\0031\0040-6\0030-6_5\003CD, kasety i płyty\0039514\0031\0031\0040-6\0030-6_6\003filmy i DVD\0039513\0031\0031\0040-6\0030-6_7\003gry planszowe i puzzle\0039515\0031\0031\0040-6\0030-6_8\003sport\0039519\0031\0031\0040-6\0030-6_9\003sprzęt turystyczny\0039531\0031\0031\004\0030-7\003Zwierzaki\0039124\0031\0031\0040-7\0030-7_0\003Wszystkie Zwierzaki\0039124\0031\0030\0040-7\0030-7_1\003psy i szczenięta\0039131\0031\0031\0040-7\0030-7_2\003koty i kocięta\0039125\0031\0031\0040-7\0030-7_3\003inne zwierzaki\0039126\0031\0031\0040-7\0030-7_4\003zgubiono lub znaleziono\0039128\0031\0031\0040-7\0030-7_5\003akcesoria dla zwierząt\0039129\0031\0031\0040-7\0030-7_6\003usługi dla zwierząt\0039130\0031\0031\004\0030-8\003Społeczność\0036\0031\0031\0040-8\0030-8_0\003Wszystkie Społeczność\0036\0031\0030\0040-8\0030-8_1\003drobne pytania i hobby\0039030\0031\0031\0040-8\0030-8_2\003sport, taniec i partnerzy do gry\0039032\0031\0031\0040-8\0030-8_3\003zespoły i muzycy\0039033\0031\0031\0040-8\0030-8_4\003wolontariat\0039227\0031\0031\0040-8\0030-8_5\003wydarzenia lokalne\0039228\0031\0031\0040-8\0030-8_6\003wymiana umiejętności\0039035\0031\0031\0040-8\0030-8_7\003zgubiono lub znaleziono\0039036\0031\0031\0040-8\0030-8_8\003przejazdy\0039037\0031\0031\0040-8\0030-8_9\003podróże\0039038\0031\0031\0040-8\0030-8_10\003dziękuję\0039039\0031\0031\0040-8\0030-8_11\003wyznania\0039084\0031\0031\0040-8\0030-8_12\003szukam starych przyjaciół\0039132\0031\0031\004\0030-9\003Oferty Pracy\0038\0031\0031\0040-9\0030-9_0\003Wszystkie Oferty Pracy\0038\0031\0030\0040-9\0030-9_1\003bar, restauracja i gastronomia\0039056\0031\0031\0040-9\0030-9_2\003biuro i administracja\0039052\0031\0031\0040-9\0030-9_3\003praca na budowie i pracownicy fizyczni\0039142\0031\0031\0040-9\0030-9_4\003fachowcy\0039203\0031\0031\0040-9\0030-9_5\003finanse i księgowość\0039050\0031\0031\0040-9\0030-9_6\003grafika i web design\0039140\0031\0031\0040-9\0030-9_7\003hostessy, modele i aktorzy\0039141\0031\0031\0040-9\0030-9_8\003hr, kadry i rekrutacja\0039053\0031\0031\0040-9\0030-9_9\003inżynierowie, technicy i architekci\0039094\0031\0031\0040-9\0030-9_10\003kierowcy i kurierzy\0039097\0031\0031\0040-9\0030-9_11\003kontrola i inwentaryzacja\0039208\0031\0031\0040-9\0030-9_12\003krawiectwo i moda\0039204\0031\0031\0040-9\0030-9_13\003marketing, media i pr\0039048\0031\0031\0040-9\0030-9_14\003praca typu mlm\0039532\0031\0031\0040-9\0030-9_15\003nauczyciele i edukacja\0039060\0031\0031\0040-9\0030-9_16\003ochrona\0039200\0031\0031\0040-9\0030-9_17\003opiekunki i nianie\0039059\0031\0031\0040-9\0030-9_18\003pielęgnacja i uroda\0039054\0031\0031\0040-9\0030-9_19\003praca dla studentów\0039206\0031\0031\0040-9\0030-9_20\003praca w hotelu\0039058\0031\0031\0040-9\0030-9_21\003prawo i prokuratura\0039049\0031\0031\0040-9\0030-9_22\003programiści, informatyka i internet\0039005\0031\0031\0040-9\0030-9_23\003służba zdrowia i farmacja\0039055\0031\0031\0040-9\0030-9_24\003spedycja\0039205\0031\0031\0040-9\0030-9_25\003sport i fitness\0039202\0031\0031\0040-9\0030-9_26\003sprzątanie i pomoc domowa\0039138\0031\0031\0040-9\0030-9_27\003sprzedaż, handel i praca w sklepie\0039061\0031\0031\0040-9\0030-9_28\003telemarketing i call center\0039098\0031\0031\0040-9\0030-9_29\003turystyka\0039207\0031\0031\0040-9\0030-9_30\003ulotki\0039201\0031\0031\0040-9\0030-9_31\003weterynaria i rolnictwo\0039095\0031\0031\0040-9\0030-9_32\003video i fotografia\0039212\0031\0031\0040-9\0030-9_33\003praca inne\0039099\0031\0031\004\0030-10\003Szukający Zatrudnienia\0039290\0031\0031\0040-10\0030-10_0\003Wszystkie Szukający Zatrudnienia\0039290\0031\0030\0040-10\0030-10_1\003gastronomia\0039291\0031\0031\0040-10\0030-10_2\003biuro i administracja\0039292\0031\0031\0040-10\0030-10_3\003pracownicy fizyczni\0039293\0031\0031\0040-10\0030-10_4\003specjaliści i technicy\0039294\0031\0031\0040-10\0030-10_5\003kierowcy i kurierzy\0039300\0031\0031\0040-10\0030-10_6\003marketing i reklama\0039304\0031\0031\0040-10\0030-10_7\003opiekunki i edukacja\0039305\0031\0031\0040-10\0030-10_8\003ochrona\0039306\0031\0031\0040-10\0030-10_9\003pielęgnacja i uroda\0039308\0031\0031\0040-10\0030-10_10\003sprzedaż i praca w sklepie\0039311\0031\0031\0040-10\0030-10_11\003szukam pracy studenckiej\0039309\0031\0031\0040-10\0030-10_12\003turystyka\0039312\0031\0031\0040-10\0030-10_13\003pozostałe\0039313\0031\0031\004\0030-11\003Usługi\0039\0031\0031\0040-11\0030-11_0\003Wszystkie Usługi\0039\0031\0030\0040-11\0030-11_1\003biura podróży\0039150\0031\0031\0040-11\0030-11_2\003współpraca biznesowa\0039325\0031\0031\0040-11\0030-11_3\003catering\0039554\0031\0031\0040-11\0030-11_4\003usługi finansowe\0039066\0031\0031\0040-11\0030-11_5\003fotografia i video\0039146\0031\0031\0040-11\0030-11_6\003graficy i usługi IT\0039234\0031\0031\0040-11\0030-11_7\003hurt i handel\0039065\0031\0031\0040-11\0030-11_8\003komputery serwis i handel\0039102\0031\0031\0040-11\0030-11_9\003usługi kurierskie\0039337\0031\0031\0040-11\0030-11_10\003nauka i edukacja\0039063\0031\0031\0040-11\0030-11_11\003mechanika i autoskup\0039145\0031\0031\0040-11\0030-11_12\003media i reklama\0039217\0031\0031\0040-11\0030-11_13\003muzycy i artyści\0039148\0031\0031\0040-11\0030-11_14\003ogrodnictwo\0039214\0031\0031\0040-11\0030-11_15\003opieka i agencje niań\0039152\0031\0031\0040-11\0030-11_16\003pielęgnacja i uroda\0039064\0031\0031\0040-11\0030-11_17\003usługi prawne\0039233\0031\0031\0040-11\0030-11_18\003przeprowadzki\0039144\0031\0031\0040-11\0030-11_19\003remont i budowa\0039101\0031\0031\0040-11\0030-11_20\003serwis i montaż\0039236\0031\0031\0040-11\0030-11_21\003sport i fitness\0039151\0031\0031\0040-11\0030-11_22\003sprzątanie\0039149\0031\0031\0040-11\0030-11_23\003śluby, wesela i przyjęcia\0039104\0031\0031\0040-11\0030-11_24\003taxi i przewozy osobowe\0039147\0031\0031\0040-11\0030-11_25\003telefony\0039341\0031\0031\0040-11\0030-11_26\003tłumaczenia i redakcja tekstu\0039216\0031\0031\0040-11\0030-11_27\003utylizacja\0039213\0031\0031\0040-11\0030-11_28\003wypożyczalnie\0039215\0031\0031\0040-11\0030-11_29\003zdrowie\0039235\0031\0031\0040-11\0030-11_30\003inne usługi\0039105\0031\0031\004\0030-12\003Moda\0039541\0031\0031\0040-12\0030-12_0\003Wszystkie Moda\0039541\0031\0030\0040-12\0030-12_1\003akcesoria i galanteria\0039542\0031\0031\0040-12\0030-12_2\003biżuteria i zegarki\0039563\0031\0031\0040-12\0030-12_3\003kosmetyki i perfumy\0039544\0031\0031\0040-12\0030-12_4\003obuwie damskie\0039596\0031\0031\0040-12\0030-12_5\003obuwie męskie\0039604\0031\0031\0040-12\0030-12_6\003odzież damska\0039565\0031\0031\0040-12\0030-12_7\003odzież męska\0039584\0031\0031\0040-12\0030-12_8\003pasmanteria\0039549\0031\0031\0040-12\0030-12_9\003torebki i torby\0039551\0031\0031\0040-12\0030-12_10\003walizki i plecaki\0039552\0031\0031\0040-12\0030-12_11\003inne ubrania\0039553\0031\0031\004";$().ready(function(){$("#searchCat").kjmenu_makeMenu({data:catdata,cssWrapperClass:'nationalSite',OnSelect:function(mitem){$("#searchCat_name").html(mitem.name+"<img border='0' src='http://pic.classistatic.com/image/pics/classifieds/spacer.gif' width='25px' height='1px'/></div>");document.frmSearchAd.CatId.value=mitem.value;$('.sfsp').remove();$('.sfasp').remove();}});});var sdata="\0030\003Polska\003202\0031\0030\004\0030-0\003Dolnośląskie\0033200007\0031\0031\0040-0\0030-0_0\003Wszystkie Dolnośląskie\0033200007\0031\0030\0040-0\0030-0_1\003Bielawa\0033200085\0031\0031\0040-0\0030-0_2\003 Bierutów\0033200435\0031\0031\0040-0\0030-0_3\003Bogatynia\0033200086\0031\0031\0040-0\0030-0_4\003 Boguszów-Gorce\0033200437\0031\0031\0040-0\0030-0_5\003Bolesławiec\0033200087\0031\0031\0040-0\0030-0_6\003 Bolków\0033200436\0031\0031\0040-0\0030-0_7\003 Brzeg Dolny\0033200438\0031\0031\0040-0\0030-0_8\003 Bystrzyca Kłodzka\0033200439\0031\0031\0040-0\0030-0_9\003 Chocianów\0033200440\0031\0031\0040-0\0030-0_10\003 Chojnów\0033200441\0031\0031\0040-0\0030-0_11\003Dzierżoniów\0033200088\0031\0031\0040-0\0030-0_12\003Głogów\0033200089\0031\0031\0040-0\0030-0_13\003Góra\0033200090\0031\0031\0040-0\0030-0_14\003 Gryfów Śląski\0033200442\0031\0031\0040-0\0030-0_15\003Jawor\0033200091\0031\0031\0040-0\0030-0_16\003 Jelcz-Laskowice\0033200443\0031\0031\0040-0\0030-0_17\003Jelenia Góra\0033200092\0031\0031\0040-0\0030-0_18\003Kamienna Góra\0033200093\0031\0031\0040-0\0030-0_19\003Karpacz\0033200094\0031\0031\0040-0\0030-0_20\003Kłodzko\0033200095\0031\0031\0040-0\0030-0_21\003 Kowary\0033200444\0031\0031\0040-0\0030-0_22\003 Kudowa-Zdrój\0033200445\0031\0031\0040-0\0030-0_23\003Legnica\0033200096\0031\0031\0040-0\0030-0_24\003Lubań\0033200097\0031\0031\0040-0\0030-0_25\003Lubin\0033200098\0031\0031\0040-0\0030-0_26\003Lwówek Śląski\0033200099\0031\0031\0040-0\0030-0_27\003Milicz\0033200100\0031\0031\0040-0\0030-0_28\003Nowa Ruda\0033200101\0031\0031\0040-0\0030-0_29\003 Oborniki Śląskie\0033200446\0031\0031\0040-0\0030-0_30\003Oława\0033200102\0031\0031\0040-0\0030-0_31\003Oleśnica\0033200103\0031\0031\0040-0\0030-0_32\003Piechowice\0033200434\0031\0031\0040-0\0030-0_33\003 Pieszyce\0033200447\0031\0031\0040-0\0030-0_34\003 Piława Górna\0033200448\0031\0031\0040-0\0030-0_35\003Polanica-Zdrój\0033200104\0031\0031\0040-0\0030-0_36\003Polkowice\0033200105\0031\0031\0040-0\0030-0_37\003 Strzegom\0033200449\0031\0031\0040-0\0030-0_38\003Strzelin\0033200107\0031\0031\0040-0\0030-0_39\003 Syców\0033200450\0031\0031\0040-0\0030-0_40\003Szklarska Poręba\0033200106\0031\0031\0040-0\0030-0_41\003Środa Śląska\0033200108\0031\0031\0040-0\0030-0_42\003Świdnica\0033200109\0031\0031\0040-0\0030-0_43\003Świebodzice\0033200110\0031\0031\0040-0\0030-0_44\003Trzebnica\0033200111\0031\0031\0040-0\0030-0_45\003Wałbrzych\0033200112\0031\0031\0040-0\0030-0_46\003Wołów\0033200113\0031\0031\0040-0\0030-0_47\003Wrocław\0033200114\0031\0031\0040-0\0030-0_48\003Ząbkowice Śląskie\0033200115\0031\0031\0040-0\0030-0_49\003Zgorzelec\0033200116\0031\0031\0040-0\0030-0_50\003 Ziębice\0033200451\0031\0031\0040-0\0030-0_51\003Złotoryja\0033200117\0031\0031\0040-0\0030-0_52\003 Żarów\0033200452\0031\0031\0040-0\0030-0_53\003 Żmigród\0033200453\0031\0031\004\0030-1\003Kujawsko - pomorskie\0033200075\0031\0031\0040-1\0030-1_0\003Wszystkie Kujawsko - pomorskie\0033200075\0031\0030\0040-1\0030-1_1\003Aleksandrów Kujawski\0033200118\0031\0031\0040-1\0030-1_2\003 Barcin\0033200454\0031\0031\0040-1\0030-1_3\003Brodnica\0033200119\0031\0031\0040-1\0030-1_4\003Bydgoszcz\0033200120\0031\0031\0040-1\0030-1_5\003Chełmno\0033200121\0031\0031\0040-1\0030-1_6\003 Chełmża\0033200455\0031\0031\0040-1\0030-1_7\003 Ciechocinek\0033200456\0031\0031\0040-1\0030-1_8\003 Gniewkowo\0033200457\0031\0031\0040-1\0030-1_9\003Golub-Dobrzyń\0033200122\0031\0031\0040-1\0030-1_10\003Grudziądz\0033200123\0031\0031\0040-1\0030-1_11\003Inowrocław\0033200124\0031\0031\0040-1\0030-1_12\003 Janikowo\0033200458\0031\0031\0040-1\0030-1_13\003 Koronowo\0033200459\0031\0031\0040-1\0030-1_14\003 Kruszwica\0033200460\0031\0031\0040-1\0030-1_15\003Lipno\0033200125\0031\0031\0040-1\0030-1_16\003Mogilno\0033200126\0031\0031\0040-1\0030-1_17\003Nakło nad Notecią\0033200127\0031\0031\0040-1\0030-1_18\003Radziejów\0033200128\0031\0031\0040-1\0030-1_19\003Rypin\0033200129\0031\0031\0040-1\0030-1_20\003Sępólno Krajeńskie\0033200130\0031\0031\0040-1\0030-1_21\003 Solec Kujawski\0033200461\0031\0031\0040-1\0030-1_22\003 Strzelno\0033200462\0031\0031\0040-1\0030-1_23\003Świecie\0033200131\0031\0031\0040-1\0030-1_24\003 Szubin\0033200463\0031\0031\0040-1\0030-1_25\003Toruń\0033200132\0031\0031\0040-1\0030-1_26\003Tuchola\0033200133\0031\0031\0040-1\0030-1_27\003Wąbrzeźno\0033200134\0031\0031\0040-1\0030-1_28\003 Więcbork\0033200464\0031\0031\0040-1\0030-1_29\003Włocławek\0033200135\0031\0031\0040-1\0030-1_30\003Żnin\0033200136\0031\0031\004\0030-2\003Lubelskie\0033200076\0031\0031\0040-2\0030-2_0\003Wszystkie Lubelskie\0033200076\0031\0030\0040-2\0030-2_1\003Bełżyce\0033200465\0031\0031\0040-2\0030-2_2\003Biała Podlaska\0033200137\0031\0031\0040-2\0030-2_3\003Biłgoraj\0033200138\0031\0031\0040-2\0030-2_4\003Chełm\0033200139\0031\0031\0040-2\0030-2_5\003Dęblin\0033200466\0031\0031\0040-2\0030-2_6\003Hrubieszów\0033200140\0031\0031\0040-2\0030-2_7\003Janów Lubelski\0033200141\0031\0031\0040-2\0030-2_8\003Krasnystaw\0033200142\0031\0031\0040-2\0030-2_9\003Kraśnik\0033200143\0031\0031\0040-2\0030-2_10\003Lubartów\0033200144\0031\0031\0040-2\0030-2_11\003Lublin\0033200145\0031\0031\0040-2\0030-2_12\003Łęczna\0033200146\0031\0031\0040-2\0030-2_13\003Łuków\0033200147\0031\0031\0040-2\0030-2_14\003Międzyrzec Podlaski\0033200467\0031\0031\0040-2\0030-2_15\003Opole Lubelskie\0033200148\0031\0031\0040-2\0030-2_16\003Parczew\0033200149\0031\0031\0040-2\0030-2_17\003Poniatowa\0033200468\0031\0031\0040-2\0030-2_18\003Puławy\0033200150\0031\0031\0040-2\0030-2_19\003Radzyń Podlaski\0033200151\0031\0031\0040-2\0030-2_20\003Ryki\0033200152\0031\0031\0040-2\0030-2_21\003Świdnik\0033200153\0031\0031\0040-2\0030-2_22\003Terespol\0033200469\0031\0031\0040-2\0030-2_23\003Tomaszów Lubelski\0033200154\0031\0031\0040-2\0030-2_24\003Włodawa\0033200155\0031\0031\0040-2\0030-2_25\003Zamość\0033200156\0031\0031\004\0030-3\003Lubuskie\0033200077\0031\0031\0040-3\0030-3_0\003Wszystkie Lubuskie\0033200077\0031\0030\0040-3\0030-3_1\003Drezdenko\0033200158\0031\0031\0040-3\0030-3_2\003Gorzów Wielkopolski\0033200157\0031\0031\0040-3\0030-3_3\003Gubin\0033200159\0031\0031\0040-3\0030-3_4\003 Kostrzyn nad Odrą\0033200470\0031\0031\0040-3\0030-3_5\003 Kożuchów\0033200471\0031\0031\0040-3\0030-3_6\003Krosno Odrzańskie\0033200160\0031\0031\0040-3\0030-3_7\003Lubsko\0033200161\0031\0031\0040-3\0030-3_8\003Międzyrzecz\0033200162\0031\0031\0040-3\0030-3_9\003Nowa Sól\0033200163\0031\0031\0040-3\0030-3_10\003 Rzepin\0033200472\0031\0031\0040-3\0030-3_11\003sulechów\0033200166\0031\0031\0040-3\0030-3_12\003Słubice\0033200164\0031\0031\0040-3\0030-3_13\003Strzelce Krajeńskie\0033200165\0031\0031\0040-3\0030-3_14\003 Skwierzyna\0033200473\0031\0031\0040-3\0030-3_15\003Sulęcin\0033200167\0031\0031\0040-3\0030-3_16\003Szprotawa\0033200168\0031\0031\0040-3\0030-3_17\003Świebodzin\0033200169\0031\0031\0040-3\0030-3_18\003 Witnica\0033200474\0031\0031\0040-3\0030-3_19\003Wschowa\0033200170\0031\0031\0040-3\0030-3_20\003Zielona Góra\0033200171\0031\0031\0040-3\0030-3_21\003Żagań\0033200172\0031\0031\0040-3\0030-3_22\003Żary\0033200173\0031\0031\004\0030-4\003Łódzkie\0033200004\0031\0031\0040-4\0030-4_0\003Wszystkie Łódzkie\0033200004\0031\0030\0040-4\0030-4_1\003Aleksandrów Łódzki\0033200174\0031\0031\0040-4\0030-4_2\003Bełchatów\0033200175\0031\0031\0040-4\0030-4_3\003Brzeziny\0033200176\0031\0031\0040-4\0030-4_4\003Głowno\0033200177\0031\0031\0040-4\0030-4_5\003 Koluszki\0033200475\0031\0031\0040-4\0030-4_6\003Konstantynów Łódzki\0033200178\0031\0031\0040-4\0030-4_7\003Kutno\0033200179\0031\0031\0040-4\0030-4_8\003Łask\0033200180\0031\0031\0040-4\0030-4_9\003Łęczyca\0033200181\0031\0031\0040-4\0030-4_10\003Łowicz\0033200182\0031\0031\0040-4\0030-4_11\003Łódź\0033200183\0031\0031\0040-4\0030-4_12\003Opoczno\0033200184\0031\0031\0040-4\0030-4_13\003Ozorków\0033200185\0031\0031\0040-4\0030-4_14\003Pabianice\0033200186\0031\0031\0040-4\0030-4_15\003Pajęczno\0033200187\0031\0031\0040-4\0030-4_16\003Piotrków Trybunalski\0033200188\0031\0031\0040-4\0030-4_17\003Poddębice\0033200189\0031\0031\0040-4\0030-4_18\003Radomsko\0033200190\0031\0031\0040-4\0030-4_19\003Rawa Mazowiecka\0033200191\0031\0031\0040-4\0030-4_20\003Sieradz\0033200192\0031\0031\0040-4\0030-4_21\003Skierniewice\0033200193\0031\0031\0040-4\0030-4_22\003 Tuszyn\0033200476\0031\0031\0040-4\0030-4_23\003Tomaszów Mazowiecki\0033200194\0031\0031\0040-4\0030-4_24\003Wieluń\0033200195\0031\0031\0040-4\0030-4_25\003Wieruszów\0033200196\0031\0031\0040-4\0030-4_26\003Zduńska Wola\0033200197\0031\0031\0040-4\0030-4_27\003 Zelów\0033200477\0031\0031\0040-4\0030-4_28\003Zgierz\0033200198\0031\0031\0040-4\0030-4_29\003 Żychlin\0033200478\0031\0031\004\0030-5\003Małopolskie\0033200003\0031\0031\0040-5\0030-5_0\003Wszystkie Małopolskie\0033200003\0031\0030\0040-5\0030-5_1\003Andrychów\0033200199\0031\0031\0040-5\0030-5_2\003Bochnia\0033200200\0031\0031\0040-5\0030-5_3\003Brzesko\0033200201\0031\0031\0040-5\0030-5_4\003Brzeszcze\0033200479\0031\0031\0040-5\0030-5_5\003Bukowina Tatrzańska\0033200202\0031\0031\0040-5\0030-5_6\003Bukowno\0033200480\0031\0031\0040-5\0030-5_7\003Chełmek\0033200481\0031\0031\0040-5\0030-5_8\003Chrzanów\0033200203\0031\0031\0040-5\0030-5_9\003Dąbrowa Tarnowska\0033200204\0031\0031\0040-5\0030-5_10\003Gorlice\0033200205\0031\0031\0040-5\0030-5_11\003Kęty\0033200206\0031\0031\0040-5\0030-5_12\003Kościelisko\0033200207\0031\0031\0040-5\0030-5_13\003Kraków\0033200208\0031\0031\0040-5\0030-5_14\003Krościenko nad Dunajcem\0033200491\0031\0031\0040-5\0030-5_15\003Krynica-Zdrój\0033200209\0031\0031\0040-5\0030-5_16\003Krzeszowice\0033200482\0031\0031\0040-5\0030-5_17\003Libiąż\0033200483\0031\0031\0040-5\0030-5_18\003Limanowa\0033200210\0031\0031\0040-5\0030-5_19\003Miechów\0033200211\0031\0031\0040-5\0030-5_20\003Mszana Dolna\0033200484\0031\0031\0040-5\0030-5_21\003Myślenice\0033200212\0031\0031\0040-5\0030-5_22\003Niepołomice\0033200485\0031\0031\0040-5\0030-5_23\003Nowy Sącz\0033200213\0031\0031\0040-5\0030-5_24\003Nowy Targ\0033200214\0031\0031\0040-5\0030-5_25\003Olkusz\0033200215\0031\0031\0040-5\0030-5_26\003Oświęcim\0033200216\0031\0031\0040-5\0030-5_27\003Piwniczna-Zdrój\0033200486\0031\0031\0040-5\0030-5_28\003Proszowice\0033200217\0031\0031\0040-5\0030-5_29\003Rabka-Zdrój\0033200487\0031\0031\0040-5\0030-5_30\003Skawina\0033200218\0031\0031\0040-5\0030-5_31\003Stary Sącz\0033200488\0031\0031\0040-5\0030-5_32\003Sucha Beskidzka\0033200219\0031\0031\0040-5\0030-5_33\003Szczawnica\0033200220\0031\0031\0040-5\0030-5_34\003Tarnów\0033200221\0031\0031\0040-5\0030-5_35\003Trzebinia\0033200222\0031\0031\0040-5\0030-5_36\003Tuchów\0033200489\0031\0031\0040-5\0030-5_37\003Wadowice\0033200223\0031\0031\0040-5\0030-5_38\003Wieliczka\0033200224\0031\0031\0040-5\0030-5_39\003Wolbrom\0033200490\0031\0031\0040-5\0030-5_40\003Zakopane\0033200225\0031\0031\004\0030-6\003Mazowieckie\0033200001\0031\0031\0040-6\0030-6_0\003Wszystkie Mazowieckie\0033200001\0031\0030\0040-6\0030-6_1\003Warszawa\0033200008\0031\0031\0040-6\0030-6_2\003Północne powiaty\0033200027\0031\0031\0040-6\0030-6_3\003Pn - wsch powiaty\0033200036\0031\0031\0040-6\0030-6_4\003Pn - zach powiaty\0033200041\0031\0031\0040-6\0030-6_5\003Południowe powiaty\0033200042\0031\0031\0040-6\0030-6_6\003Pd - wsch powiaty\0033200043\0031\0031\0040-6\0030-6_7\003Pd - zach powiaty\0033200044\0031\0031\0040-6\0030-6_8\003Wschodnie powiaty\0033200045\0031\0031\0040-6\0030-6_9\003Zachodnie powiaty\0033200046\0031\0031\004\0030-7\003Opolskie\0033200078\0031\0031\0040-7\0030-7_0\003Wszystkie Opolskie\0033200078\0031\0030\0040-7\0030-7_1\003Brzeg\0033200226\0031\0031\0040-7\0030-7_2\003Głubczyce\0033200227\0031\0031\0040-7\0030-7_3\003Grodków\0033200526\0031\0031\0040-7\0030-7_4\003Kędzierzyn-Koźle\0033200228\0031\0031\0040-7\0030-7_5\003Kluczbork\0033200229\0031\0031\0040-7\0030-7_6\003Krapkowice\0033200230\0031\0031\0040-7\0030-7_7\003Namysłów\0033200231\0031\0031\0040-7\0030-7_8\003Niemodlin\0033200527\0031\0031\0040-7\0030-7_9\003Nysa\0033200232\0031\0031\0040-7\0030-7_10\003Olesno\0033200233\0031\0031\0040-7\0030-7_11\003Opole\0033200234\0031\0031\0040-7\0030-7_12\003Ozimek\0033200528\0031\0031\0040-7\0030-7_13\003Paczków\0033200529\0031\0031\0040-7\0030-7_14\003Praszka\0033200530\0031\0031\0040-7\0030-7_15\003Prudnik\0033200235\0031\0031\0040-7\0030-7_16\003Strzelce Opolskie\0033200236\0031\0031\0040-7\0030-7_17\003Zawadzkie\0033200531\0031\0031\0040-7\0030-7_18\003Zdzieszowice\0033200532\0031\0031\004\0030-8\003Podkarpackie\0033200079\0031\0031\0040-8\0030-8_0\003Wszystkie Podkarpackie\0033200079\0031\0030\0040-8\0030-8_1\003Brzozów\0033200237\0031\0031\0040-8\0030-8_2\003Dębica\0033200238\0031\0031\0040-8\0030-8_3\003Jarosław\0033200239\0031\0031\0040-8\0030-8_4\003Jasło\0033200240\0031\0031\0040-8\0030-8_5\003Kolbuszowa\0033200241\0031\0031\0040-8\0030-8_6\003Krosno\0033200242\0031\0031\0040-8\0030-8_7\003Lesko\0033200243\0031\0031\0040-8\0030-8_8\003Leżajsk\0033200244\0031\0031\0040-8\0030-8_9\003Lubaczów\0033200245\0031\0031\0040-8\0030-8_10\003Łańcut\0033200246\0031\0031\0040-8\0030-8_11\003Mielec\0033200247\0031\0031\0040-8\0030-8_12\003Nisko\0033200248\0031\0031\0040-8\0030-8_13\003Nowa Dęba\0033200533\0031\0031\0040-8\0030-8_14\003Przemyśl\0033200249\0031\0031\0040-8\0030-8_15\003Przeworsk\0033200250\0031\0031\0040-8\0030-8_16\003Ropczyce\0033200251\0031\0031\0040-8\0030-8_17\003Rzeszów\0033200252\0031\0031\0040-8\0030-8_18\003Sanok\0033200253\0031\0031\0040-8\0030-8_19\003Sędziszów Małopolski\0033200534\0031\0031\0040-8\0030-8_20\003Stalowa Wola\0033200254\0031\0031\0040-8\0030-8_21\003Strzyżów\0033200255\0031\0031\0040-8\0030-8_22\003Tarnobrzeg\0033200256\0031\0031\0040-8\0030-8_23\003Ustrzyki Dolne\0033200257\0031\0031\004\0030-9\003Podlaskie\0033200080\0031\0031\0040-9\0030-9_0\003Wszystkie Podlaskie\0033200080\0031\0030\0040-9\0030-9_1\003Augustów\0033200258\0031\0031\0040-9\0030-9_2\003Białystok\0033200259\0031\0031\0040-9\0030-9_3\003Bielsk Podlaski\0033200260\0031\0031\0040-9\0030-9_4\003 Czarna Białostocka\0033200535\0031\0031\0040-9\0030-9_5\003 Dąbrowa Białostocka\0033200536\0031\0031\0040-9\0030-9_6\003Grajewo\0033200261\0031\0031\0040-9\0030-9_7\003Hajnówka\0033200262\0031\0031\0040-9\0030-9_8\003Kolno\0033200263\0031\0031\0040-9\0030-9_9\003Łapy\0033200264\0031\0031\0040-9\0030-9_10\003Łomża\0033200265\0031\0031\0040-9\0030-9_11\003Mońki\0033200266\0031\0031\0040-9\0030-9_12\003Sejny\0033200267\0031\0031\0040-9\0030-9_13\003Siemiatycze\0033200268\0031\0031\0040-9\0030-9_14\003Sokółka\0033200269\0031\0031\0040-9\0030-9_15\003Suwałki\0033200270\0031\0031\0040-9\0030-9_16\003 Wasilków\0033200537\0031\0031\0040-9\0030-9_17\003Wysokie Mazowieckie\0033200271\0031\0031\0040-9\0030-9_18\003Zambrów\0033200272\0031\0031\004\0030-10\003Pomorskie\0033200005\0031\0031\0040-10\0030-10_0\003Wszystkie Pomorskie\0033200005\0031\0030\0040-10\0030-10_1\003Bytów\0033200407\0031\0031\0040-10\0030-10_2\003Chojnice\0033200408\0031\0031\0040-10\0030-10_3\003Człuchów\0033200409\0031\0031\0040-10\0030-10_4\003Czersk\0033200539\0031\0031\0040-10\0030-10_5\003Gdańsk\0033200072\0031\0031\0040-10\0030-10_6\003Gdynia\0033200073\0031\0031\0040-10\0030-10_7\003Gniew\0033200543\0031\0031\0040-10\0030-10_8\003Hel\0033200410\0031\0031\0040-10\0030-10_9\003Jastarnia\0033200411\0031\0031\0040-10\0030-10_10\003Jastrzębia Góra\0033200412\0031\0031\0040-10\0030-10_11\003Kartuzy\0033200413\0031\0031\0040-10\0030-10_12\003Karwia\0033200414\0031\0031\0040-10\0030-10_13\003Kościerzyna\0033200415\0031\0031\0040-10\0030-10_14\003Krynica Morska\0033200416\0031\0031\0040-10\0030-10_15\003Kwidzyn\0033200417\0031\0031\0040-10\0030-10_16\003Łeba\0033200418\0031\0031\0040-10\0030-10_17\003Lębork\0033200419\0031\0031\0040-10\0030-10_18\003Malbork\0033200420\0031\0031\0040-10\0030-10_19\003Miastko\0033200538\0031\0031\0040-10\0030-10_20\003Nowy Dwór Gdański\0033200421\0031\0031\0040-10\0030-10_21\003Pelplin\0033200541\0031\0031\0040-10\0030-10_22\003Prabuty\0033200540\0031\0031\0040-10\0030-10_23\003Pruszcz Gdański\0033200422\0031\0031\0040-10\0030-10_24\003Puck\0033200423\0031\0031\0040-10\0030-10_25\003Reda\0033200424\0031\0031\0040-10\0030-10_26\003Rumia\0033200425\0031\0031\0040-10\0030-10_27\003Skarszewy\0033200542\0031\0031\0040-10\0030-10_28\003Słupsk\0033200426\0031\0031\0040-10\0030-10_29\003Sopot\0033200074\0031\0031\0040-10\0030-10_30\003Starogard Gdański\0033200427\0031\0031\0040-10\0030-10_31\003Stegna\0033200428\0031\0031\0040-10\0030-10_32\003Sztum\0033200429\0031\0031\0040-10\0030-10_33\003Sztutowo\0033200544\0031\0031\0040-10\0030-10_34\003Tczew\0033200430\0031\0031\0040-10\0030-10_35\003Ustka\0033200431\0031\0031\0040-10\0030-10_36\003Wejherowo\0033200432\0031\0031\0040-10\0030-10_37\003Władysławowo\0033200433\0031\0031\004\0030-11\003Śląskie\0033200002\0031\0031\0040-11\0030-11_0\003Wszystkie Śląskie\0033200002\0031\0030\0040-11\0030-11_1\003Będzin\0033200273\0031\0031\0040-11\0030-11_2\003Bielsko-Biała\0033200274\0031\0031\0040-11\0030-11_3\003Bieruń\0033200275\0031\0031\0040-11\0030-11_4\003 Blachownia\0033200545\0031\0031\0040-11\0030-11_5\003Bytom\0033200277\0031\0031\0040-11\0030-11_6\003Chorzów\0033200278\0031\0031\0040-11\0030-11_7\003Cieszyn\0033200279\0031\0031\0040-11\0030-11_8\003 Czechowice-Dziedzice\0033200546\0031\0031\0040-11\0030-11_9\003 Czeladź\0033200547\0031\0031\0040-11\0030-11_10\003 Czerwionka-Leszczyny\0033200548\0031\0031\0040-11\0030-11_11\003Częstochowa\0033200280\0031\0031\0040-11\0030-11_12\003Dąbrowa Górnicza\0033200281\0031\0031\0040-11\0030-11_13\003Gliwice\0033200282\0031\0031\0040-11\0030-11_14\003 Imielin\0033200549\0031\0031\0040-11\0030-11_15\003Jastrzębie-Zdrój\0033200283\0031\0031\0040-11\0030-11_16\003Jaworzno\0033200284\0031\0031\0040-11\0030-11_17\003 Kalety\0033200550\0031\0031\0040-11\0030-11_18\003 Knurów\0033200551\0031\0031\0040-11\0030-11_19\003Katowice\0033200285\0031\0031\0040-11\0030-11_20\003Kłobuck\0033200286\0031\0031\0040-11\0030-11_21\003 Lędziny\0033200552\0031\0031\0040-11\0030-11_22\003Lubliniec\0033200287\0031\0031\0040-11\0030-11_23\003 Łaziska Górne\0033200553\0031\0031\0040-11\0030-11_24\003Mikołów\0033200288\0031\0031\0040-11\0030-11_25\003Mysłowice\0033200289\0031\0031\0040-11\0030-11_26\003Myszków\0033200290\0031\0031\0040-11\0030-11_27\003 Orzesze\0033200554\0031\0031\0040-11\0030-11_28\003Piekary Śląskie\0033200291\0031\0031\0040-11\0030-11_29\003 Poręba\0033200555\0031\0031\0040-11\0030-11_30\003Pszczyna\0033200292\0031\0031\0040-11\0030-11_31\003 Pszów\0033200556\0031\0031\0040-11\0030-11_32\003 Pyskowice\0033200557\0031\0031\0040-11\0030-11_33\003Racibórz\0033200293\0031\0031\0040-11\0030-11_34\003 Radlin\0033200558\0031\0031\0040-11\0030-11_35\003 Radzionków\0033200559\0031\0031\0040-11\0030-11_36\003Ruda Śląska\0033200294\0031\0031\0040-11\0030-11_37\003Rybnik\0033200295\0031\0031\0040-11\0030-11_38\003 Rydułtowy\0033200560\0031\0031\0040-11\0030-11_39\003Siemianowice Śląskie\0033200296\0031\0031\0040-11\0030-11_40\003 Skoczów\0033200561\0031\0031\0040-11\0030-11_41\003Sosnowiec\0033200297\0031\0031\0040-11\0030-11_42\003Świętochłowice\0033200298\0031\0031\0040-11\0030-11_43\003Szczyrk\0033200299\0031\0031\0040-11\0030-11_44\003Tarnowskie Góry\0033200300\0031\0031\0040-11\0030-11_45\003Tychy\0033200301\0031\0031\0040-11\0030-11_46\003 Ustroń\0033200562\0031\0031\0040-11\0030-11_47\003Wisła\0033200302\0031\0031\0040-11\0030-11_48\003Wodzisław Śląski\0033200303\0031\0031\0040-11\0030-11_49\003 Wojkowice\0033200563\0031\0031\0040-11\0030-11_50\003Zabrze\0033200304\0031\0031\0040-11\0030-11_51\003Zawiercie\0033200305\0031\0031\0040-11\0030-11_52\003Żory\0033200306\0031\0031\0040-11\0030-11_53\003Żywiec\0033200307\0031\0031\004\0030-12\003Świętokrzyskie\0033200082\0031\0031\0040-12\0030-12_0\003Wszystkie Świętokrzyskie\0033200082\0031\0030\0040-12\0030-12_1\003Busko-Zdrój\0033200308\0031\0031\0040-12\0030-12_2\003Jędrzejów\0033200309\0031\0031\0040-12\0030-12_3\003Kazimierza Wielka\0033200310\0031\0031\0040-12\0030-12_4\003Kielce\0033200311\0031\0031\0040-12\0030-12_5\003Końskie\0033200312\0031\0031\0040-12\0030-12_6\003Opatów\0033200313\0031\0031\0040-12\0030-12_7\003Ostrowiec Świętokrzyski\0033200314\0031\0031\0040-12\0030-12_8\003Pińczów\0033200315\0031\0031\0040-12\0030-12_9\003Połaniec\0033200564\0031\0031\0040-12\0030-12_10\003Sandomierz\0033200316\0031\0031\0040-12\0030-12_11\003Skarżysko-Kamienna\0033200317\0031\0031\0040-12\0030-12_12\003Starachowice\0033200318\0031\0031\0040-12\0030-12_13\003Staszów\0033200319\0031\0031\0040-12\0030-12_14\003Suchedniów\0033200565\0031\0031\0040-12\0030-12_15\003Włoszczowa\0033200320\0031\0031\004\0030-13\003Warmińsko-mazurskie\0033200083\0031\0031\0040-13\0030-13_0\003Wszystkie Warmińsko-mazurskie\0033200083\0031\0030\0040-13\0030-13_1\003Bartoszyce\0033200321\0031\0031\0040-13\0030-13_2\003Biskupiec\0033200322\0031\0031\0040-13\0030-13_3\003Braniewo\0033200323\0031\0031\0040-13\0030-13_4\003Dobre Miasto\0033200324\0031\0031\0040-13\0030-13_5\003Działdowo\0033200325\0031\0031\0040-13\0030-13_6\003Elbląg\0033200326\0031\0031\0040-13\0030-13_7\003Ełk\0033200327\0031\0031\0040-13\0030-13_8\003Giżycko\0033200328\0031\0031\0040-13\0030-13_9\003Gołdap\0033200329\0031\0031\0040-13\0030-13_10\003Iława\0033200330\0031\0031\0040-13\0030-13_11\003Kętrzyn\0033200331\0031\0031\0040-13\0030-13_12\003Lidzbark Warmiński\0033200332\0031\0031\0040-13\0030-13_13\003 Lubawa\0033200566\0031\0031\0040-13\0030-13_14\003Mikołajki\0033200333\0031\0031\0040-13\0030-13_15\003 Morąg\0033200567\0031\0031\0040-13\0030-13_16\003Mrągowo\0033200334\0031\0031\0040-13\0030-13_17\003Nidzica\0033200335\0031\0031\0040-13\0030-13_18\003Nowe Miasto Lubawskie\0033200336\0031\0031\0040-13\0030-13_19\003Olecko\0033200337\0031\0031\0040-13\0030-13_20\003Olsztyn\0033200338\0031\0031\0040-13\0030-13_21\003 Olsztynek\0033200568\0031\0031\0040-13\0030-13_22\003 Orneta\0033200569\0031\0031\0040-13\0030-13_23\003Ostróda\0033200339\0031\0031\0040-13\0030-13_24\003 Pasłęk\0033200570\0031\0031\0040-13\0030-13_25\003Pisz\0033200340\0031\0031\0040-13\0030-13_26\003Szczytno\0033200341\0031\0031\0040-13\0030-13_27\003Węgorzewo\0033200342\0031\0031\004\0030-14\003Wielkopolskie\0033200006\0031\0031\0040-14\0030-14_0\003Wszystkie Wielkopolskie\0033200006\0031\0030\0040-14\0030-14_1\003Chodzież\0033200343\0031\0031\0040-14\0030-14_2\003Czarnków\0033200344\0031\0031\0040-14\0030-14_3\003Gniezno\0033200345\0031\0031\0040-14\0030-14_4\003Gostyń\0033200346\0031\0031\0040-14\0030-14_5\003Grodzisk Wielkopolski\0033200347\0031\0031\0040-14\0030-14_6\003Jarocin\0033200348\0031\0031\0040-14\0030-14_7\003Jastrowie\0033200571\0031\0031\0040-14\0030-14_8\003Kalisz\0033200349\0031\0031\0040-14\0030-14_9\003Kępno\0033200350\0031\0031\0040-14\0030-14_10\003Koło\0033200351\0031\0031\0040-14\0030-14_11\003Konin\0033200352\0031\0031\0040-14\0030-14_12\003Kostrzyn\0033200572\0031\0031\0040-14\0030-14_13\003Kościan\0033200353\0031\0031\0040-14\0030-14_14\003Kórnik\0033200573\0031\0031\0040-14\0030-14_15\003Krotoszyn\0033200354\0031\0031\0040-14\0030-14_16\003Leszno\0033200355\0031\0031\0040-14\0030-14_17\003Luboń\0033200356\0031\0031\0040-14\0030-14_18\003Międzychód\0033200357\0031\0031\0040-14\0030-14_19\003Mosina\0033200358\0031\0031\0040-14\0030-14_20\003Murowana Goślina\0033200359\0031\0031\0040-14\0030-14_21\003Nowy Tomyśl\0033200360\0031\0031\0040-14\0030-14_22\003Oborniki\0033200361\0031\0031\0040-14\0030-14_23\003Opalenica\0033200574\0031\0031\0040-14\0030-14_24\003Ostrów Wielkopolski\0033200362\0031\0031\0040-14\0030-14_25\003Ostrzeszów\0033200363\0031\0031\0040-14\0030-14_26\003Piła\0033200364\0031\0031\0040-14\0030-14_27\003Pleszew\0033200365\0031\0031\0040-14\0030-14_28\003Pniewy\0033200575\0031\0031\0040-14\0030-14_29\003Pobiedziska\0033200576\0031\0031\0040-14\0030-14_30\003Poznań\0033200366\0031\0031\0040-14\0030-14_31\003Puszczykowo\0033200577\0031\0031\0040-14\0030-14_32\003Rawicz\0033200367\0031\0031\0040-14\0030-14_33\003Rogoźno\0033200578\0031\0031\0040-14\0030-14_34\003Słupca\0033200368\0031\0031\0040-14\0030-14_35\003Swarzędz\0033200369\0031\0031\0040-14\0030-14_36\003Szamotuły\0033200370\0031\0031\0040-14\0030-14_37\003Śrem\0033200371\0031\0031\0040-14\0030-14_38\003Środa Wielkopolska\0033200372\0031\0031\0040-14\0030-14_39\003Trzcianka\0033200373\0031\0031\0040-14\0030-14_40\003Trzemeszno\0033200579\0031\0031\0040-14\0030-14_41\003Turek\0033200374\0031\0031\0040-14\0030-14_42\003Wągrowiec\0033200375\0031\0031\0040-14\0030-14_43\003Witkowo\0033200580\0031\0031\0040-14\0030-14_44\003Wolsztyn\0033200376\0031\0031\0040-14\0030-14_45\003Wronki\0033200581\0031\0031\0040-14\0030-14_46\003Września\0033200377\0031\0031\0040-14\0030-14_47\003Złotów\0033200378\0031\0031\004\0030-15\003Zachodniopomorskie\0033200084\0031\0031\0040-15\0030-15_0\003Wszystkie Zachodniopomorskie\0033200084\0031\0030\0040-15\0030-15_1\003Barlinek\0033200379\0031\0031\0040-15\0030-15_2\003Białogard\0033200380\0031\0031\0040-15\0030-15_3\003Cedynia\0033200381\0031\0031\0040-15\0030-15_4\003Choszczno\0033200382\0031\0031\0040-15\0030-15_5\003Czaplinek\0033200586\0031\0031\0040-15\0030-15_6\003Darłowo\0033200383\0031\0031\0040-15\0030-15_7\003Dębno\0033200384\0031\0031\0040-15\0030-15_8\003Drawno\0033200385\0031\0031\0040-15\0030-15_9\003Drawsko Pomorskie\0033200386\0031\0031\0040-15\0030-15_10\003Goleniów\0033200387\0031\0031\0040-15\0030-15_11\003Gryfice\0033200388\0031\0031\0040-15\0030-15_12\003Gryfino\0033200389\0031\0031\0040-15\0030-15_13\003Kamień Pomorski\0033200390\0031\0031\0040-15\0030-15_14\003Kołobrzeg\0033200391\0031\0031\0040-15\0030-15_15\003Koszalin\0033200392\0031\0031\0040-15\0030-15_16\003Łobez\0033200393\0031\0031\0040-15\0030-15_17\003Międzyzdroje\0033200394\0031\0031\0040-15\0030-15_18\003Mielno\0033200395\0031\0031\0040-15\0030-15_19\003Myślibórz\0033200396\0031\0031\0040-15\0030-15_20\003Nowogard\0033200397\0031\0031\0040-15\0030-15_21\003Police\0033200398\0031\0031\0040-15\0030-15_22\003Połczyn-Zdrój\0033200582\0031\0031\0040-15\0030-15_23\003Pyrzyce\0033200399\0031\0031\0040-15\0030-15_24\003Sławno\0033200400\0031\0031\0040-15\0030-15_25\003Stargard Szczeciński\0033200401\0031\0031\0040-15\0030-15_26\003Szczecin\0033200402\0031\0031\0040-15\0030-15_27\003Szczecinek\0033200403\0031\0031\0040-15\0030-15_28\003Świdwin\0033200404\0031\0031\0040-15\0030-15_29\003Świnoujście\0033200405\0031\0031\0040-15\0030-15_30\003Trzebiatów\0033200583\0031\0031\0040-15\0030-15_31\003Wałcz\0033200406\0031\0031\0040-15\0030-15_32\003Wolin\0033200584\0031\0031\0040-15\0030-15_33\003Złocieniec\0033200585\0031\0031\004";var provinceSearchInputHtml='<input name="isProvinceSearch" type="hidden" value="true" />';$().ready(function(){function getURLParameter(name){return decodeURIComponent((location.href.match(RegExp("[QQ]"+name+'Z(.+?)(QQ|$)'))||[,null])[1]);}
var isProvinceSearch=getURLParameter('isProvinceSearch');document.frmSearchAd.Location.value=Math.abs(3200208);if(isProvinceSearch=='true'){var isProvinceSearchInput=$('input[name=isProvinceSearch]');if(isProvinceSearchInput.length>0){isProvinceSearchInput.val('true');}
else{$('#frmSearchAd').append(provinceSearchInputHtml);}}
$("#searchLoc").kjmenu_makeMenu({data:sdata,zindex:90000,cssWrapperClass:'nationalSite',OnSelect:function(mitem){var provinceSearchInput=$('input[name=isProvinceSearch]');if(mitem.value<-1){if(provinceSearchInput.length>0){provinceSearchInput.val('true');}
else{$('#frmSearchAd').append(provinceSearchInputHtml);}}
else{if(provinceSearchInput.length>0){provinceSearchInput.remove();}}
$("#searchLoc_name").html(mitem.name+"<img border='0' src='http://pic.classistatic.com/image/pics/classifieds/spacer.gif' width='25px' height='1px'/>");document.frmSearchAd.Location.value=Math.abs(mitem.value);$('.sfsp').remove();}});});addOnUnloadFunction('disableElement("searchAdGo")');var autoOptions={maxChars:4,hideLabel:'Ukryj',timeout:1,maxEntries:7,containerStyleClass:'keySpan',submitOnlick:true,baseUrl:"http://ac.classistatic.com/ac/10028/202/pl_PL/"};$(document).ready(function(){$("input.keyword").autocomplete1(autoOptions);$("#searchAdGo").click(function(){gAnalyticsPushForSearch("Click-Search",$(".newHeader input[name=distance]").val());});$("form#frmSearchAd").submit(function(){if($("#autoComp")[0].value==="Czego szukasz...?"){$("#autoComp")[0].value="";}
$("#searchAdGo").attr("disabled","true");return true;});});function gAnalyticsPushForSearch(srchType,numValue){}
var browsedata="\004\0030\003Nieruchomości\003http://www.gumtree.pl/fp-nieruchomosci/krakow/c2l3200208\004\0030\003Sprzedam\003http://www.gumtree.pl/fp-sprzedam/krakow/c4l3200208\004\0030\003Oferty Pracy\003http://www.gumtree.pl/fp-oferty-pracy/krakow/c8l3200208\004\0030\003Motoryzacja\003http://www.gumtree.pl/fp-motoryzacja/krakow/c5l3200208\004\0030\003Szukający Zatrudnienia\003http://www.gumtree.pl/fp-szukajacy-zatrudnienia/krakow/c9290l3200208\004\0030\003Moda\003http://www.gumtree.pl/fp-moda/krakow/c9541l3200208\004\0030\003Łodzie i Pojazdy wodne\003http://www.gumtree.pl/fp-lodzie-i-pojazdy-wodne/krakow/c9218l3200208\004\0030\003Elektronika\003http://www.gumtree.pl/fp-elektronika/krakow/c9237l3200208\004\0030\003Usługi\003http://www.gumtree.pl/fp-uslugi/krakow/c9l3200208\004\0030\003Dla Dziecka\003http://www.gumtree.pl/fp-dla-dziecka/krakow/c9459l3200208\004\0030\003Zwierzaki\003http://www.gumtree.pl/fp-zwierzaki/krakow/c9124l3200208\004\0030\003Sport i Rozrywka\003http://www.gumtree.pl/fp-sport-i-rozrywka/krakow/c9490l3200208\004\0030\003Społeczność\003http://www.gumtree.pl/fp-spolecznosc/krakow/c6l3200208\004\0030\003Oddam za darmo\003http://www.gumtree.pl/fp-krakow/l3200208?AdType=2&PriceAlternative=3\004\0030\003Wymiana/zamiana\003http://www.gumtree.pl/fp-krakow/l3200208?PriceAlternative=5";$(document).ready(function(){$("#AreaHomeTab,#SiteHomeTab").kjmenu_makeMenu({data:browsedata,OnSelect:function(mitem){document.location.replace(mitem.value);}});$("#changeLocDiv").click(function(){$.ajax({url:'http://www.gumtree.pl/c-GetLocation?CatId=0&PageName=',dataType:'script'});});});function trackHomeTabDropdown(type){var statisticUrl="";if(type=="tabname"){statisticUrl='http://www.gumtree.pl/c-Statistic?StatType=';}else if(type=="link"){statisticUrl='http://www.gumtree.pl/c-Statistic?StatType=HomeTabDropdownCount';}
statisticUrl=statisticUrl+'&ms='+new Date().getTime();$.get(statisticUrl);return true;}
var KNS=KNS||{};KNS.popWordSel='.floatLeft30px a';KNS.miscLabels=KNS.miscLabels||{};KNS.miscLabels.keyWordsLabelEn="Popular";$(document).ready(function(){$(KNS.popWordSel).click(function(){Kj.Ga.trackEventsinGA({category:'Clicks on '+KNS.miscLabels.keyWordsLabelEn+' Searches',action:'clicked word # '+($(KNS.popWordSel).index($(this))+1),opt_label:$(this).attr('href'),track_on_area_level:true});});});$(document).ready(function(){Kj.View.initViewAdActions({adId:'607878925',reportdata:"\0032\003Oszustwo/Zabronione\0032\004\0033\003Duplikat/Spam\0033\004\0035\003Nieaktualne\0035\004\0031\003W złej kategorii\0031\004\003r\003Wpisz powód...\003r",url:"http://www.gumtree.pl/c-illegalAdPanel"});});function doFlag(url){if(typeof(url)=='undefined'){return false;}
$("#pagestatus_new").css("display","");$.get('/c-ReportProblemByAjax?'+url,function(data){$("#pagestatus_new").html(data);});}
var currentModal;$(document).ready(function(){$('#doMisCat').click(function(e){var options={onOpen:function(){appendModalFrame();$("#modalframe").attr("src","http://www.gumtree.pl/c-wrongCategoryPanel");$('#modalFrameLayer').css('height',227);$('#modalframe').css('height',227);$('#modalFrameLayer').show();e.preventDefault();this.open(true);currentModal=this;}};$('#modalFrameLayer').modal(options);e.preventDefault();});});$(document).ready(function(){$('#doIllegalAd').click(function(e){var options={onOpen:function(){appendModalFrame();$("#modalframe").attr("src","http://www.gumtree.pl/c-illegalAdPanel");$('#modalFrameLayer').height(0);$('#modalFrameLayer').show();e.preventDefault();this.open(true);currentModal=this;}};$('#modalFrameLayer').modal(options);e.preventDefault();});});function scaleIllegalAdModal(height){$('#modalframe').css('height',height);$('#modalFrameLayer').css('height',height);$('#modalFrameLayer').css('margin-top',height/2*-1);}
function hideModal(){$('#modalframe').remove();currentModal.close(true);currentModal=null;}
function appendModalFrame(){$("#modalFrameLayer").append('<iframe name="modalframe" id="modalframe" width="100%" scrolling="no" frameborder="0" src="http://pic.classistatic.com/image/pics/classifieds/loading2.gif"></iframe>');}
function submitCategory(action,l1,l2){url="AdId=607878925&ViolationType=1";if(action=="submit"){try{url+="&L1CatId="+l1+"&L2CatId="+l2;}catch(err){}}
doFlag(url);hideModal();setTimeout('goTop()',800);}
function submitIllegal(action,email,msg){url="AdId=607878925&ViolationType=4";if(action=="submit"){try{url+="&Email="+email+"&Description="+msg;}catch(err){alert(err);}}
else{hideModal();return false;}
doFlag(url);hideModal();setTimeout('goTop()',800);}
function goTop(){$(document).scrollTop(0);}
var KNS=KNS||{};KNS.options=KNS.options||{};$(document).ready(function(){Kj.View.initThumbnailNavigator({pics:{fullImgUrl:'http://www.gumtree.pl/c-ViewAdLargeImage?AdId=607878925&Keyword=krakow',images:['http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_35.JPG','http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/gacAAOSwxCxT195J/$_35.JPG','http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/Tu0AAOSwPe1T195v/$_35.JPG','http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/EbQAAOSw7NNT1956/$_35.JPG','http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/lKUAAOSwRLZT196P/$_35.JPG','http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/a78AAOSwEK9T196h/$_35.JPG','http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/bj4AAOSwEK9T1963/$_35.JPG','http://i.ebayimg.com/00/s/MTAwMFg3NTA=/z/JKUAAOSwQItT197E/$_35.JPG'],speed:400},totalCount:"8",videoCount:"0",catPath:"Properties/flat+%2F+house+for+rent"});});$(".view").load(function(){$(".imageStack").addClass("hideImageBackGrd");});$("img").load(function(){$(".imageStack2").addClass("hideImageBackGrd");});$(document).ready(function(){var init=false;$('.viewmap-link').click(function(){if(!init)
{init=true;Kj.Map.displayMap({canvas:"gmap",lat:"50.0067142",longitude:"19.889592100000073",addrTitle:'Adres',directionText:'Zobacz wskazówki dojazdu',adMarkers:[{addr:"Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska",pinType:"addr"}],hl:"pl",zoom:13},"http://maps.googleapis.com/maps/api/js?&client=gme-marktplaats&sensor=false&v=3.10");}});});$(function(){$(".viewmap-link").click(function(e){e.preventDefault();$.cachedScript("http://include.classistatic.com/include/e884/c3js/classifieds/rel1//common/jQuery/jquery.ui.dialog-min.js").done(function(script,textStatus){$("#viewmap-modal").dialog({width:800,modal:true,dialogClass:"dialog-view-image",title:"<span class='fLeft'>Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska</span>",open:function(){$(".ui-icon-closethick").html(" ");},close:function(){$('meta[name="DCSext.page"]').attr("content","ViewAd");}});});});});var catpathvar={'sa606759499':'Properties/flat+%2F+house+for+rent','sa607359596':'Properties/flat+%2F+house+for+rent','sa607937278':'Properties/flat+%2F+house+for+rent','sa607315619':'Properties/flat+%2F+house+for+rent','sa607888553':'Properties/flat+%2F+house+for+rent'};$(document).ready(function(){$(".salink").click(function(e){Kj.Ga.trackEventsinGA({category:'SimilarAds',action:'SimilarAdClick',opt_label:catpathvar[$(e.target).parents('.salink').attr('id')],track_on_area_level:true});});});$(document).ready(function(){Kj.View.initMaskedPhone({catpath:'Properties/flat+%2F+house+for+rent',adId:"607 878 925",phoneRateLimiterEnabled:false,phoneLoggingEnabled:false,tryAgainLaterImg:"http://pic.classistatic.com/image/pics/classifieds/pl-PL/TryAgainLater.png",phoneImg:"http://ext.classistatic.com/imagesvc/txt2Img/GUEZdyU-ESoSSRTaZ2_migZN4p6ySNa6tvalAmTk8edZ_tEvl1pIsw0YiCmruWY7lfOS2C9fMOrYlqYYRLYuxlqlNZxEKQ3z3L3xROIA6g9VkYpUgu8BCpbDtF9G3dtl697ZG_0GJzgYQ8lfczz8grOcLGgqeZM5lmO6v_2TQ0kpivdwLq4RALJ0PcV45o6zjKe2rHWMA6IXrG9ukmK0xJeQ03Tyg_0iAwuL9yw9Rx8",hiddenPhoneImageUrl:"http://www.gumtree.pl/c-PhoneImage?ImageId=a89f3840607878925a53d9d43bz542720f259",phoneClickUrl:"http://www.gumtree.pl/c-UpdateClickCount?AdId=607878925&counterType=phone",isGAUpdated:false});});KNS.options.copyme="CopyMe";KNS.options.catpath='Properties/flat+%2F+house+for+rent';KNS.options.isGAUpdated=false;$(document).ready(function(){Kj.View.initReplyToAd(KNS.options);});$(document).ready(function(){Kj.View.initWebsiteClk({websiteClickUrl:'http://www.gumtree.pl/c-UpdateClickCount?AdId=607878925&counterType=website'});});$(document).ready(function(){$('#AreaHomeTab,#SiteHomeTab').click(function(e){trackHomeTabDropdown('tabname')});$('#AreaHomeText,#SiteHomeText').addClass('browse');var freeIcon=$('#freeIcon2');if(freeIcon.length>0){freeIcon.click(function(e){document.location='c-SelectCategory';return false;});}
$('.BigSearch').attachHoverPopup('#CategoryDropdown');});Kj.initReady({});
// End-TAIL JS
</script>
<!-- customJs -->
<!-- End of HtmlPageTail -->
<div id="flashCookie"></div>
<div id="myFavorites-panel"> </div>
<script>
Kj.initFavoritesFunctionality({domain:'www.gumtree.pl',panelActivated:'true',staticsPath:'http://include.classistatic.com/include/e884/c3js/classifieds/rel1/'});
</script>
</body></html>
"""
 
OFFER2_HTML = u"""
<!DOCTYPE html PUBLIC "-//W3C//DTD OFFER_HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
 
<html xmlns="http://www.w3.org/1999/xhtml"  xmlns:fb="http://www.facebook.com/2008/fbml"> 
<head>
<title>Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego</title>
<meta http-equiv="X-UA-Compatible" content="IE=9"/>
<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<meta name="description" content="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego, mieszkania i domy do wynajęcia, ogłoszenia drobne na Gumtree"/>
<meta name="uniq_GUMTREE_POLAND_page_token_name" content="ViewAd"/>
<meta property="og:image" content="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_35.JPG"/>
<meta property="og:title" content="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/przytulne-2-pokojowe-35m-ruczaj-babinskiego-607878925"/>
<meta property="og:description" content="Do wynajęcia od zaraz 2-pokojowe mieszkanie przy ul. Babińskiego 23b ( I piętro). Mieszkanie ma 2 pokoje ( w tym 1 przechodni), kuchnie, łazienkę, przedpokój i balkon z widokiem. Okolica bardzo spokojna. Przystanek autobusowy &quot;Babińskiego&quot; 2 min. od "/>
<meta property="og:locality" content="Kraków"/>
<meta property="og:site_name" content="Gumtree Polska"/>
<meta property="og:country-name" content="Poland"/>
<link rel="canonical" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/przytulne-2-pokojowe-35m-ruczaj-babinskiego-607878925"/>
<link rel="SHORTCUT ICON" href="http://pic.classistatic.com/image/pics/classifieds/gumtreeFavicon.ico">
<link href="http://include.classistatic.com/include/e884/c3css/pages/ViewAdShared-min.css" rel="stylesheet" type="text/css">
<link href="http://include.classistatic.com/include/e884/c3css/brands/gumtree/PL/all-pl.css" rel="stylesheet" type="text/css">
<script type="text/javascript">
//<!--
var picsPath = "http://pic.classistatic.com/image/pics/classifieds/";
var staticPath = "http://include.classistatic.com/include/e884/c3js/classifieds/rel1/";
var debugNonProdStaticPathPrefix = "s_isProduction => true, s_localStaticPath => null, m_isSecure => false, s_localSecureStaticPath => null, nonProdStaticPathPrefix => ";
//-->
</script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/shared_pages/flashChecker.js"></script>
<script src="http://www.google.com/jsapi"></script>
<noscript>
<style type="text/css">
.jsonly {display:none;}
.collapseWithJS {display:block;}
.collapseWithJS_inline {display:inline;}
</style>
</noscript>
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['siteTracker._setAccount', 'UA-9157637-1']);
_gaq.push(['siteTracker._setDomainName', '.gumtree.pl']);
_gaq.push(['siteTracker._setSessionCookieTimeout', 1800000]);
_gaq.push(['siteTracker._setCampaignCookieTimeout', 15768000000]);
_gaq.push(['siteTracker._setVisitorCookieTimeout', 63072000000]);
_gaq.push(['siteTracker._trackPageview', '/ViewAd/properties/flat+%2f+house+for+rent/attribute']);
</script>
<script type="text/javascript">
(function() {
var ga = document.createElement("script");
ga.type = "text/javascript"; ga.async = true;
ga.src = ("https:" == document.location.protocol ? "https://ssl" : "http://www") + ".google-analytics.com/ga.js";
var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<script type="text/javascript">
var mpx_custom = {
new_mpcl: 'p;krakow;9008;Nieruchomo%C5%9Bci;l3;1;820;p;;n;607878925;http%3A%2F%2Fwww.gumtree.pl%2Fcp-mieszkania-i-domy-do-wynajecia%2Fkrakow%2Fprzytulne-2-pokojowe-35m-ruczaj-babinskiego-607878925%3FfeaturedAd%3Dtrue',
new_mpvl: document.referrer
}
</script>
</head>
<body>
<div id="main">
<div id="top">
<a name="#top"></a>
<div id="mediaplex_tracking"></div>
<script type="text/javascript">
(function() {
var mpxtag = document.createElement('script'); mpxtag.type = 'text/javascript'; mpxtag.async = true;
mpxtag.src = ('https:' == document.location.protocol
? 'https://secure.img-cdn.mediaplex.com/0/9860/56583/Kijiji-Poland_mp_pvt_brand_landing_ns_2013-04-30.js'
: 'http://img-cdn.mediaplex.com/0/9860/56583/Kijiji-Poland_mp_pvt_brand_landing_ns_2013-04-30.js');
var smpx = document.getElementsByTagName('script')[0]; smpx.parentNode.insertBefore(mpxtag, smpx);
})();
</script>
<!-- Start of HtmlPageHeader_03. This ftl is used for national site for Team 9 team -->
<script> var IsNC2_On = true; </script>
<script> var IsAdIdsSite_On = false; </script>
<table class="tbleColpse newHeader nationalSite">
<tr>
<td class="national-logo-area">
<div>
<a href="http://www.gumtree.pl" >
<img src="http://pic.classistatic.com/image/pics/classifieds/pl-PL/logo-gumtree.png" width="68" height="76" border="0" alt="Polska ">
</a>
</div> </td>
<td class="header-curve">
<div class="header-curve-top">&nbsp;</div>
<div class="header-curve-bottom">&nbsp;</div>
</td>
<td class="header-curve-space">
<div class="header-top-bg">&nbsp;</div>
<div class="header-bottom-bg">&nbsp;</div>
</td>
<td class="v-top">
<table width="100%" class="tbleColpse">
<tr>
<td class="navTabs-new h-top">
<div class="mainTabs">
<a href="http://www.gumtree.pl/c-SelectCategory" class="tabLink" >
<div id="SelectCategoryTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div> + Dodaj ogłoszenie</div>
</div></div></div>
</a>
<a href="http://www.gumtree.pl" class="tabLink" >
<div id="SiteHomeTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div id="SiteHomeText">Kategorie</div>
</div></div></div>
</a>
<a href="http://www.gumtree.pl/c-DealerDirectory" class="tabLink" >
<div id="DealerDirectoryTab" class="tab"><div class="tab-right"><div class="tab-mid"> <div>Katalog sprzedawców</div>
</div></div></div>
</a>
</div>
</td>
<td class="lang h-top">
<div class="menuTop">
<ul>
<div id="withoutGreetings">
<li>
<!--<a href="https://secure.gumtree.pl/s-SignIn?rup=ViewAd&ruq=AdId%3D607878925" id="log_out" >here:Zaloguj się</a>-->
<span onclick="clickEncoded('aHR0cHM6Ly9zZWN1cmUuZ3VtdHJlZS5wbC9zLVNpZ25Jbj9ydXA9Vmlld0FkJnJ1cT1BZElkJTNENjA3ODc4OTI1')" class="sd-link">Zaloguj się</span>
<span class="bar">&nbsp;|&nbsp;</span>
</li>
<li>
<!--<a href="https://secure.gumtree.pl/s-StartRegistration?rup=ViewAd&ruq=AdId%3D607878925" id="log_out" >here:Zarejestruj się</a>-->
<span onclick="clickEncoded('aHR0cHM6Ly9zZWN1cmUuZ3VtdHJlZS5wbC9zLVN0YXJ0UmVnaXN0cmF0aW9uP3J1cD1WaWV3QWQmcnVxPUFkSWQlM0Q2MDc4Nzg5MjU=')" class="sd-link">Zarejestruj się</span>
<span class="bar">&nbsp;|&nbsp;</span>
</li>
<li>
<!--<a href="http://www.gumtree.pl/c-ManageMyAds" id="log_out" >here:Moje Gumtree</a>-->
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtTWFuYWdlTXlBZHM=')" class="sd-link">Moje Gumtree</span>
</li>
</div>
</ul>
</div>
</td>
</tr>
</table>
<noscript>
<style>
.msgbar{
padding-top:5px;
}
</style>
</noscript>
<table class="search-area tbleColpse header-bottom-bg">
<tr>
<td style="padding-right:10px" nowrap="true" valign="middle">
<table class="tbleColpse rel-p" width="100%" >
<tr>
<td nowrap="true" align="left">
<table class="tbleColpse">
<form action="http://www.gumtree.pl/f-SearchAdRedirect" method="get" name="frmSearchAd" id="frmSearchAd" class="searchform">
<input type="hidden" name="isSearchForm" value="true">
<tr>
<td><div class="ww_table_left"></div></td>
<td align="left" >
<table class="tbleColpse" >
<!--
<tr>
<td class="ww_table">
<div class="toplbl">here:Czego szukasz...?</div>
</td>
</tr>
-->
<tr>
<td class="ww_table" style="padding-right:10px">
<div class="flt">
<span class="left-what"></span>
<span class="keySpan lf">
<input title="Czego szukasz...?" id="autoComp" type="text" name="Keyword" value="" class="keyword center-what" autocomplete="off"/>
</span>
<span class="right-what"></span>
</div>
</td>
</tr>
</table>
</td>
<td class="ww_table" style="padding-right:10px">
<div id="searchCat" class="jsonly kjmenu_main_wrap">
<div class="left-all-cat"></div>
<div id="searchCat_name" class="center-all-cat">Wszystkie kategorie<img border="0" src="http://pic.classistatic.com/image/pics/classifieds/spacer.gif" width="25px" height="1px"/></div>
<div class="button-arrow"></div>
</div>
<input class="jsonly" type="hidden" name="CatId" value="0"/>
</td>
<td class="ww_table">
<div id="searchLoc" class="jsonly kjmenu_main_wrap">
<div class="left-all-cat"></div>
<div id="searchLoc_name" class="center-all-cat">Kraków<img border="0" src="http://pic.classistatic.com/image/pics/classifieds/spacer.gif" width="25px" height="1px"/></div>
<div class="button-arrow"></div>
</div>
<input class="jsonly" type="hidden" name="Location" value=""/>
</td>
<td class="ww_table" style="padding-left:10px">
<span class="left-search"></span>
<input id="searchAdGo" type="submit" value="Szukaj" class="searchButton" />
<span class="right-search"></span>
</td>
<td><div class="ww_table_right"></div></td>
</tr>
</form>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
</td>
</tr>
</table>
<div id="CategoryDropdown" class="popupWindow">
<ul class="catlistdropdown">
<li class="item">
<span class="cursptr" id="catId0" onClick="swapCat(this,'0');">Wszystkie ogłoszenia</span>
</li>
<li class="item">
<span class="cursptr" id="catId2" onClick="swapCat(this,'2');">Nieruchomości</span>
</li>
<li class="item">
<span class="cursptr" id="catId4" onClick="swapCat(this,'4');">Sprzedam</span>
</li>
<li class="item">
<span class="cursptr" id="catId8" onClick="swapCat(this,'8');">Oferty Pracy</span>
</li>
<li class="item">
<span class="cursptr" id="catId5" onClick="swapCat(this,'5');">Motoryzacja</span>
</li>
<li class="item">
<span class="cursptr" id="catId9290" onClick="swapCat(this,'9290');">Szukający Zatrudnienia</span>
</li>
<li class="item">
<span class="cursptr" id="catId9541" onClick="swapCat(this,'9541');">Moda</span>
</li>
<li class="item">
<span class="cursptr" id="catId9218" onClick="swapCat(this,'9218');">Łodzie i Pojazdy wodne</span>
</li>
<li class="item">
<span class="cursptr" id="catId9237" onClick="swapCat(this,'9237');">Elektronika</span>
</li>
<li class="item">
<span class="cursptr" id="catId9" onClick="swapCat(this,'9');">Usługi</span>
</li>
<li class="item">
<span class="cursptr" id="catId9459" onClick="swapCat(this,'9459');">Dla Dziecka</span>
</li>
<li class="item">
<span class="cursptr" id="catId9124" onClick="swapCat(this,'9124');">Zwierzaki</span>
</li>
<li class="item">
<span class="cursptr" id="catId9490" onClick="swapCat(this,'9490');">Sport i Rozrywka</span>
</li>
<li class="item">
<span class="cursptr" id="catId6" onClick="swapCat(this,'6');">Społeczność</span>
</li>
</ul>
</div>
<div class=popWords>
<div class="floatLeft30px">
Popularne
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/radzikowskiego/c9008" title="radzikowskiego">radzikowskiego</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/wieczysta/c9008" title="wieczysta">wieczysta</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/radzymin/c9008" title="radzymin">radzymin</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/strzeszyn/c9008" title="strzeszyn">strzeszyn</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/saska/c9008" title="saska">saska</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/jab%C5%82onna/c9008" title="jabłonna">jabłonna</a>
</div>
<div class="floatLeft30px">
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/sosnowiec/c9008" title="sosnowiec">sosnowiec</a>
</div>
</div>
<div class="greyBottom300">
</div>
<div id="pagestatus_new" style="">
</div>
</div>
<div id="middle" class="page_viewad">
<div class="VAStyleA">
<div id="viewad_header">
<table class="tbleColpse viewadhdr">
<tr>
<td valign="top">
<div id="breadcrumbVIP">
<div itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
<a href="http://www.gumtree.pl" itemprop="url">
<span itemprop="title">Polska</span>
</a> &gt; <a href="http://www.gumtree.pl/fp-nieruchomosci/krakow/c2l3200208" itemprop="url">
<span itemprop="title">Nieruchomości</span>
</a>
>
<a href="http://www.gumtree.pl/fp-mieszkania-i-domy-do-wynajecia/krakow/c9008l3200208" itemprop="url">
<span itemprop="title">mieszkania i domy do wynajęcia</span>
</a>
&gt; Nr referencyjny ogłoszenia 607878925
</div>
</div>
<div><div id='div-gpt-ad-1363883804543-leader' style="margin:0 auto;text-align:center;">
</div>
<div id='div-gpt-ad-vip-topbanner' style='text-align:center;margin:0px auto'></div></div>
</td>
<td align="right" valign="top">
</td>
</tr>
</table>
<table class="viewadtitle">
<tr>
<td class="viewadtitleL viewadtitleLComm">
<table class="tbleColpse">
<tr>
<td >
<div >
<h1 class="" id="preview-local-title" >
<!-- google_ad_section_start -->Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego<!-- google_ad_section_end -->
</h1>
</div>
</td>
</tr>
</table>
</td>
<td class="viewadaction">
<ul id="viewAd-actions" class="viewAd-actions" >
<li><span nowrap="true" class="jsonly wl_star_off" title="Zachowaj ogłoszenie">&nbsp;&nbsp;&nbsp;&nbsp;<span class="watchText">Zachowaj</span></span></li>
<li class="pipe">|</li>
<li>
<span class="s2f">
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtU2VuZFRvRnJpZW5kP0FkSWQ9NjA3ODc4OTI1')" class="sudo-link">Udostępnij</span>
</span>
</li>
<li class="pipe">|</li>
<li>
<!-- rt:5001 - Removing icon labels if Print has empty content in ViewAd.xml-->
<span class="print">
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtUHJpbnRBZD9BZElkPTYwNzg3ODkyNQ==', '_blank')" class="sudo-link">Drukuj</span>
</span>
</li>
<li class="pipe">|</li>
<li> <span class="jsonly" id="reportAd_name">Zgłoś ogłoszenie<span>&nbsp;&nbsp;&nbsp;</span></span>
<div class="modal" id="modalFrameLayer"></div>
</li>
</ul>
</td>
</tr>
</table>
</div>
<noscript>
<style type="text/css">
.jsonly {
display:none;
}
</style>
</noscript>
<table class="adcontent tblClpsePad">
<tr>
<td>
<table width="100%" class="tblClpsePad"
>
<tr>
<td class="adImg">
<div style="margin-bottom:5px;">
<table cellpadding="0" cellspacing="0" border="0" class="viewad_images viewad_frame_tbl" >
<tr>
<td class="viewad_images viewad_frame_fill">
<table width="100%" height="3" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=bottom class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_tl viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_images viewad_frame_tm viewad_images viewad_frame_brand1" style="font-size:3px">
<div class="viewad_images viewad_frame_fill"> </div>
</td>
<td valign=bottom class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_tr viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td class="viewad_images viewad_frame_m viewad_images viewad_frame_brand2" style="margin:0px">
<table width="100%" class="gallery viewad_frame_brand2 tbleColpse viewadimgcontr">
<tr>
<td align=middle class="imageStack " imggal='main'>
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtVmlld0FkTGFyZ2VJbWFnZT9BZElkPTYwNzg3ODkyNSZLZXl3b3JkPWtyYWtvdw==')" class="sudo-link" title='Zoom'>
<img class="view" title="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego" alt="Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego image0" src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_35.JPG" border="0" />
</span>
</td>
</tr>
</table>
<center>
<table class="img-next-prev tbleColpse">
<tr>
<td class="jsonly">
<div class="prev" imggal='prev'>&nbsp; </div>
</td>
<td style="padding:0px 10px 0px 10px">
<span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtVmlld0FkTGFyZ2VJbWFnZT9BZElkPTYwNzg3ODkyNSZLZXl3b3JkPWtyYWtvdw==')" class="sudo-link" title='Zoom' imggal='viewimg'>
<div class="view-large">
<div> Powiększ obraz </div>
</div>
</span>
</td>
<td class="jsonly">
<div class="next" imggal='next'>&nbsp; </div>
</td>
</tr>
</table>
</center>
<table class='navs' cellpadding="0" cellspacing="0" border="0">
<tr class="imageNavs">
</tr>
<tr class="imageNavs">
<td imggal="thumb" imgindx="0" class="ni active">
<img src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="1" class="ni">
<img src="http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/gacAAOSwxCxT195J/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="2" class="ni">
<img src="http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/Tu0AAOSwPe1T195v/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="3" class="ni">
<img src="http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/EbQAAOSw7NNT1956/$_14.JPG" border="0"/>
</td>
</tr>
<tr class="imageNavs">
<td imggal="thumb" imgindx="4" class="ni">
<img src="http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/lKUAAOSwRLZT196P/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="5" class="ni">
<img src="http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/a78AAOSwEK9T196h/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="6" class="ni">
<img src="http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/bj4AAOSwEK9T1963/$_14.JPG" border="0"/>
</td>
<td imggal="thumb" imgindx="7" class="ni">
<img src="http://i.ebayimg.com/00/s/MTAwMFg3NTA=/z/JKUAAOSwQItT197E/$_14.JPG" border="0"/>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td class="viewad_images viewad_frame_fill">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=top class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_bl viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_images viewad_frame_bm viewad_images viewad_frame_brand1" style="font-size:3px;height:3px">
<div class="viewad_images viewad_frame_fill"> </div>
</td>
<td valign=top class="viewad_images viewad_frame_fill">
<div class="viewad_images viewad_frame_br viewad_images viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
</table>
</div>
</td>
<td valign="top" width="99%">
<div style="font-weight:normal">
<table cellpadding="0" cellspacing="0" border="0" class="viewad_frame_tbl" style="min-width:260px;">
<tr>
<td class="viewad_frame_fill">
<table width="100%" height="3" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=bottom class="viewad_frame_fill">
<div class="viewad_frame_tl viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_frame_tm viewad_frame_brand1" style="font-size:3px">
<div class="viewad_frame_fill"> </div>
</td>
<td valign=bottom class="viewad_frame_fill">
<div class="viewad_frame_tr viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td class="viewad_frame_m viewad_frame_brand2" style='padding:0px 2px 0px 2px' style="margin:0px"> <table id="attributeTable" border="0" cellpadding="3" cellspacing="0" width="100%">
<col/><col width="99%"/>
<tbody>
<tr>
<td nowrap valign=top class="first_col first_row " >Data dodania
</td>
<td class="first_row" > 29/07/2014
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Cena
</td>
<td style='font-weight:bold'> Zł  950,00
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Adres
</td>
<td itemscope itemtype="http://schema.org/Place"> Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska
<br>
<span class="viewmap-link sudo-link">Pokaż mapę</span>
</td>
</tr> <div id="viewmap-modal" style="display:none"> <div id="gmap" style="width:100%; height:507px" valign="top">
<noscript>
<strong>Adres:</strong> Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska<br>
</noscript>
</div>
</div>
<tr>
<td nowrap valign=top class="first_col " >Do wynajęcia przez
</td>
<td > Właściciel
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Rodzaj nieruchomości
</td>
<td > Mieszkanie
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Liczba pokoi
</td>
<td > 2 pokoje
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Wielkość (m2)
</td>
<td > 36
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Liczba łazienek
</td>
<td > 1 łazienka
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Parking
</td>
<td > Ulica
</td>
</tr>
<tr>
<td nowrap valign=top class="first_col " >Przyjazne zwierzakom
</td>
<td > Tak
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td class="viewad_frame_fill">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>
<td valign=top class="viewad_frame_fill">
<div class="viewad_frame_bl viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
<td width="99%" class="viewad_frame_bm viewad_frame_brand1" style="font-size:3px;height:3px">
<div class="viewad_frame_fill"> </div>
</td>
<td valign=top class="viewad_frame_fill">
<div class="viewad_frame_br viewad_frame_brand1" style="font-size:3px;height:3px"> </div>
</td>
</tr>
</table>
</td>
</tr>
</table>
<div id="ad-desc" class="ad-desc" class="marginTop10px" >
<!-- google_ad_section_start -->
<span id="preview-local-desc">
Do wynajęcia od zaraz 2-pokojowe mieszkanie przy ul. Babińskiego 23b ( I piętro). Mieszkanie ma 2 pokoje ( w tym 1 przechodni), kuchnie, łazienkę, przedpokój i balkon z widokiem. Okolica bardzo spokojna. Przystanek autobusowy "Babińskiego" 2 min. od bloku, przystanek "Zachodnia" 7 min. Dojazd do centrum zajmuje ok. 30 min. Do miasta można również dojeżdżać busikami jeżdżącymi ze Skawiny, jest się wówczas w okolicach centrum( busiki jeżdżą pod Dworzec lub pod Pocztę Główną) w ok. 20 min.<br/>Przed blokiem jest miejsce do parkowania. Z balkonu ładny widok, żadnych bloków na horyzoncie:) Mieszkanie przytulne, remontowane kilka lat temu. Mieszkanie w pełni wyposażone (pralka, lodówka, kuchenka, piekarnik). Nowe okna, ogrzewanie miejskie. Opłaty miesięczne to ok. 450 zł przy 2 osobach (czynsz administracyjny + prąd).
</span>
<!-- google_ad_section_end -->
</div>
<div class="cenvis">
<span class="visits">Wizyty: 383 </span>
</div>
</div>
</td>
</tr>
<tr>
</tr>
</table>
<br/>
<style>
.page_viewad #viewAd-actions .s2f, #viewad_header #viewAd-actions .s2f { background-image: url("http://pic.classistatic.com/image/site/ca/icons/facebook.gif"); }
.stack-adsense-title { background-color: #fdeb6b; } .weburl { text-overflow:ellipsis; overflow: hidden; white-space: nowrap; width: 260px } .right_logo_box.brand_border { text-align: center; height: auto; }
.viewAdImgTitle { height: auto; }
</style>
<div class="similarads clearfix">
<div class="titlebar">
Podobne ogłoszenia
</div>
<div class="maindiv">
<div class="contentdiv">
<div class="imagediv">
<a id="sa606759499" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ekskluzywny-apartament-3-pokoje-75m2-obok-dworca-okazja-606759499">
<img src="http://i.ebayimg.com/00/s/ODAyWDEwMjQ=/z/N6cAAOSw9NxTvmZu/$_14.JPG" border="0" />
</a>
</div>
<a id="sa606759499" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/ekskluzywny-apartament-3-pokoje-75m2-obok-dworca-okazja-606759499">
<div class="pricediv">
Zł  3 000,00
</div>
<div class="titlediv">
Ekskluzywny apartament 3-pokoje, 75m2, obok dworca OKAZJA
</div>
<div class="datediv">
Dodane: 10/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607359596" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/plac-matejki-stary-kleparz-kawalerka-sw-filipa-607359596">
<img src="http://i.ebayimg.com/00/s/MTAwMFg2Njc=/z/89YAAOSwKPNTzCvI/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607359596" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/plac-matejki-stary-kleparz-kawalerka-sw-filipa-607359596">
<div class="pricediv">
Zł  1 100,00
</div>
<div class="titlediv">
PLAC MATEJKI, STARY KLEPARZ, kawalerka, Św. Filipa
</div>
<div class="datediv">
Dodane: 20/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607937278" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/nowoczesne-apartament-75m2-ul-bronowicka-2600pln-607937278">
<img src="http://i.ebayimg.com/00/s/NDI2WDY0MA==/z/b~IAAOSwVFlT2SZr/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607937278" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/nowoczesne-apartament-75m2-ul-bronowicka-2600pln-607937278">
<div class="pricediv">
Zł  2 600,00
</div>
<div class="titlediv">
Nowoczesne apartament 75m2,ul.Bronowicka 2600pln
</div>
<div class="datediv">
Dodane: 30/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607315619" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/super-lokalizacja-ul-grzegorzecka-jeden-pokoj-607315619">
<img src="http://i.ebayimg.com/00/s/NDMyWDY0MA==/z/PxEAAOSwq7JTyrb2/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607315619" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/super-lokalizacja-ul-grzegorzecka-jeden-pokoj-607315619">
<div class="pricediv">
Zł  1 350,00
</div>
<div class="titlediv">
Super lokalizacja, ul. Grzegórzecka, jeden pokój
</div>
<div class="datediv">
Dodane: 19/07/2014
</div>
</a>
</div>
<div class="contentdiv">
<div class="imagediv">
<a id="sa607888553" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-krakow-krowodrza-25m2-nr-9848-607888553">
<img src="http://i.ebayimg.com/00/s/NDIyWDY0MA==/z/RfsAAOSwVFlT2Edv/$_14.JPG" border="0" />
</a>
</div>
<a id="sa607888553" class="salink" href="http://www.gumtree.pl/cp-mieszkania-i-domy-do-wynajecia/krakow/mieszkanie-krakow-krowodrza-25m2-nr-9848-607888553">
<div class="pricediv">
Zł  1 000,00
</div>
<div class="titlediv">
Mieszkanie Kraków Krowodrza 25m2 (nr: 9848)
</div>
<div class="datediv">
Dodane: 30/07/2014
</div>
</a>
</div>
</div>
</div>
</div>
<br/>
<div id="googsense"></div>
</td>
<td class="viewadrightcol" style="margin:0px;padding:0px 0px 0px 15px">
<div class="alternate-box">
<div class="alternate-contact-info">DANE KONTAKTOWE</div>
<div class="alternate-phone-box">
<div class="alternate-phone-icon">&nbsp;</div>
<div id="phn-text">
<span class="alternate-phone-number">796...</span>
<div class="alternate-show-phone-bar">
<span class="alt-ph-hover"><span class="alternate-show-phone-bar-left">&nbsp;</span><span class="alternate-show-phone-bar-center"><a class="alternate-show-phone-number" href="javascript:">Pokaż numer telefonu</a></span><span class="alternate-show-phone-bar-right">&nbsp;</span></span>
</div>
</div>
</div>
<div id='phoneclicktracking'></div>
<noscript>
<div style="padding-bottom:5px;">
<div class='PhoneIcon' style="padding-left:20px"><img src="http://ext.classistatic.com/imagesvc/txt2Img/GUEZdyU-ESoSSRTaZ2_migZN4p6ySNa6tvalAmTk8edZ_tEvl1pIsw0YiCmruWY7lfOS2C9fMOrYlqYYRLYuxlqlNZxEKQ3z3L3xROIA6g9VkYpUgu8BCpbDtF9G3dtl697ZG_0GJzgYQ8lfczz8grOcLGgqeZM5lmO6v_2TQ0kpivdwLq4RALJ0PcV45o6zjKe2rHWMA6IXrG9ukmK0xJeQ03Tyg_0iAwuL9yw9Rx8" style="border:none;" /> </div>
</div>
</noscript> <div class="alternate-email-label">Skontaktuj się przez e-mail</div>
<div class="email_block brand_border">
<div id="viewad_email">
<form id="ReplyToAdForm" action="/c-ViewAd" method="post" name="viewadfrm">
<noscript>
<style type="text/css">
#ReplyToAdForm .first-input div {
padding-left : 0px;
background : transparent;
}
</style>
</noscript>
<input type="hidden" name="AdId" value="607878925"/>
<input type="hidden" name="Submit" value="true"/>
<span id="MTNew" >
</span>
<span id="CDOld" >
<div id="SenderEmailAddress_field" class="first-field" >
<div class="first-input">
<a name="FromEmailAddress"></a>
<div class="input-div">
<input type="text" name="FromEmailAddress" value=""
id="SenderEmailAddress"
title="Twój e-mail"
style="width:100%"
class="reply-field"
size="30"
/>
</div>
</div>
</div>
</span>
<span id="MTOld" >
<div class="first-field" >
<div formfield="label" class="first-label ">
<span id="lblEmailText" ><noscript>Wiadomość</noscript></span>
</div>
<div class="first-input">
<a name="EmailText"></a>
<div class="input-div">
<textarea name="EmailText"
cols="25"
title="Wiadomość"
style="width:290px; margin-top:7px;"
class="reply-field"
rows="4"
></textarea>
</div>
</div>
</div>
</span>
<span id="CDNew">
</span>
<div class="alternate-checkbox">
<input type="checkbox" name="CopyMe" value="checked" checked/> Wyślij mi kopię e-maila
</div>
<div class="alternate-submit-box">
<span class="alternate-submit-left">&nbsp;</span><input type="submit" id="send" value='WYŚLIJ E-MAIL' class="alternate-submit-center"/><span class="alternate-submit-right">&nbsp;</span>
<div style="clear:both;"></div>
</div>
</form>
<div class="alternate-help-text">
Klikając „Wyślij”, wyrażasz zgodę na nasze <span onclick="clickEncoded('L3AtVGVybXNBbmRDb25kaXRpb25z')" class="sudo-link" >Zasady korzystania</span> i <span onclick="clickEncoded('L3AtUHJpdmFjeQ==')" class="sudo-link" >Politykę prywatności</span>. Twoja wiadomość zostanie wysłana do ogłoszeniodawcy i nie będzie widoczna publicznie.
</div>
</div>
</div>
<div class="alternate-line">&nbsp;</div>
<div class="alternate-posted-by-box">
<div class="alternate-view-all-ads"> <span class="alternate-active-since">
Aktywny od: lip 2014
</span>
</div>
<div class="alternate-top-p2">&nbsp;</div>
<div class="alternate-icon-poster ">&nbsp;</div>
<div class="alternate-poster-info"> <span onclick="clickEncoded('aHR0cDovL3d3dy5ndW10cmVlLnBsL2MtUG9zdGVyc090aGVyQWRzLVcwUVFVc2VySWRaOTM0NjE5NzE=')" class="sudo-link"> Zobacz wszystkie ogłoszenia tego użytkownika Gumtree
</span>
</div>
<div>&nbsp;</div>
</div>
</div>
<div><p>
<center>
<script jsinline type="text/javascript">
mpt = new Date();
mpts = mpt.getTimezoneOffset() + mpt.getTime();
if (!document.layers) {
document.writeln("<scr"+"ipt type=\"text\/javascript\" src=\"http:\/\/altfarm.mediaplex.com\/ad\/js\/10832-110408-23165-0\?mpt=" + mpts + "&mpvc=\"><\/script>");
} else {
document.write("<a href=\"http://altfarm.mediaplex.com/ad/ck/10832-110408-23165-0?mpt=" + mpts + "\"><img src=\"http://altfarm.mediaplex.com/ad/bn/10832-110408-23165-0?mpt=" + mpts
+ "\" alt=\"Click Here\" border=\"0\"></a>" );
}
</script>
<noscript>
<a href="http://altfarm.mediaplex.com/ad/nc/10832-110408-23165-0">
<img src="http://altfarm.mediaplex.com/ad/nb/10832-110408-23165-0"
alt="Click Here" border="0">
</a>
</noscript>
</center>
<p>
<!-- Ad section -->
<div id='div-gpt-ad-1318934199048-0' style='width:300px; height:250px;margin:6px auto'></div>
<div id='div-gpt-ad-1318934199048-1' style='width:300px; height:250px;margin:6px auto'></div></div>
<br/>
<br/>
</td>
</tr>
</table>
</div>
</div>
<div id="bottom">
<div class="footer">
<div>
<link type="text/css" rel="stylesheet" href="https://securepic.classistatic.com/image/site/au/global_footer/new_global_footer.css" />
<style type="text/css">
.footer {
border-top: 0px solid #BEC3C7;
margin: 0px 0px 0px 15px;
padding: 10px 0 10px 0;
}
.footer li {
list-style:none;
display: list-item;
color: #676B5C;
font-size:11px;
margin:0;
padding:0 5px 0 0;
border-right: 0px solid #ffffcc;
}
.get-to-know-us,.explore-gumtree,.legalbits,.tips-help,.blog-latest,.gumtree-elsewhere{
display:inline;
float:left;
}
.get-to-know-us{
margin-left:10px;
}
.blog-latest{
margin-left:0px;
}
#footer-links > div {
margin-right: 10px;
width: 150px;
}
#footer-links .gumtree-elsewhere {
width: 120px;
}
#footer .social-facebook,
#footer .social-twitter,
#footer .social-google,
#footer .social-pinterest,
#footer .social-youtube{ display:block; margin-bottom:3px; height:18px; line-height:18px; padding-left:20px; background-repeat:no-repeat; background-position:left center; background-size:18px 18px; }
</style>
<div id="footer" class="footer">
<div id="footer-links" class="container">
<div class="gumtree-legal" style="display:inline">
<h3><a href="http://www.gumtree.pl">
<img src="http://pic.classistatic.com/image/site/au/global_footer/footer_logo.gif" border="0" alt=""></a></h3>
</div>
<div class="get-to-know-us">
<h3>Poznaj nas</h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=122">O Gumtree</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?category=5">Zasady zamieszczania ogłoszeń</a></li>
</ul>
</div>
<div class="explore-gumtree">
<h3>Odkryj więcej</h3>
<ul>
<li><a href="http://info.gumtree.pl/promowanie/index.html">Promowanie ogłoszeń</a></li>
<li><a href="http://www.gumtree.pl/c-PopularSearches">Popularne wyszukiwania</a></li>
</ul>
</div>
<div class="legalbits">
<h3>Sprawy prawne</h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=120">Zasady korzystania</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?article=121">Polityka Prywatności</a></li>
</ul>
</div>
<div class="tips-help">
<h3>Pomoc i porady </h3>
<ul>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php">Pomoc</a></li>
<li><a href="http://gumtreehelp.com/pl/knowledgebase.php?category=7">Pozostań bezpiecznym </a></li>
<li><a href="http://gumtreehelp.com/pl/index.php">Napisz do nas </a></li>
<li><a href="http://blog.gumtree.pl/">Gumtree Blog </a></li>
</ul>
</div>
<div class="gumtree-elsewhere">
<h3>Śledź nas</h3>
<ul>
<li><a class="social-facebook" href="https://www.facebook.com/GumtreePolska" target="_blank">Facebook</a></li>
<li><a class="social-google" href="https://plus.google.com/103950977256553454134/posts" rel="publisher" target="_blank">Google+</a></li>
<li><a class="social-twitter" href="https://twitter.com/gumtreepolska" target="_blank">Twitter</a></li>
<li><a class="social-youtube" href="http://www.youtube.com/user/GumtreePolska" target="_blank">YouTube</a></li>
<li><a class="social-pinterest" href="http://pinterest.com/gumtreepolska" target="_blank">Pinterest</a></li>
</ul>
</div>
<div class="blog-latest">
</div>
</div>
<!-- Start Alexa Certify Javascript -->
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=wS4fj1a4ZP00g+" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
<div id="copyright">&nbsp;</div>
</div>
<div class="cpyrt">
Copyright © 2014 eBay International AG
</div>
<!--<style> html .fb_share_link { margin-left: 5px; padding:0 0 0 20px; height:16px; background:url(http://b.static.ak.fbcdn.net/images/share/facebook_share_icon.gif?8:26981) no-repeat top left; }</style>
<a href="http://altfarm.mediaplex.com/ad/ck/9860-90999-23165-0?mpt=1&mpre=http%3A//www.facebook.com/share.php%3Fu%3Dhttp%3A//gumtree.pl.gumtree.pl/c-ViewAd%3FAdId%3D607878925" onclick="return fbs_click()" target="_blank" class="fb_share_link"><font size="2">Dołącz do Fanów na Facebook'u</font></a>&nbsp;&nbsp;|<img src="http://pic.classistatic.com/image/site/au/twitter_16x16_FFFAEE.GIF" hspace="5"/><a href="http://twitter.com/gumtreepolska/" target="_blank"><font size="2">Śledź nas na Twitterze</font></a>-->
</div>
</div>
</div>
<!-- Start of HtmlPageTail -->
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/common/common-min.js"></script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1//pages/viewAd-min.js"></script>
<script type="text/javascript" language="JavaScript" src="http://include.classistatic.com/include/e884/c3js/classifieds/rel1/shared_pages/mapServices-min.js"></script>
<div id="OandN" class="modal">
<table cellpadding="0" cellspacing="0" width="100%">
<tr>
<td class="modalHeading">
<div class="layerTitleText"></div>
<div class="closeBtn close" title="Close">&nbsp;</div>
</td>
</tr>
<tr class="layerContent">
<td>
<div id="OandNContent" class="OandNCont">
<div class="OandNData">
<b>Oferty:</b> Ogłoszenia z ceną mogą zawierać również opcję złożenia oferty. Złożone oferty nie są wiążące. Ogłoszeniodawca otrzymuje szczegóły oferty po jej złożeniu. Ogłoszeniodawca może odpowiedzieć na ofertę lub nie.
<br/><br/></br>
<b>Powiadomienia:</b> Podczas składania oferty możesz zdecydować się na codzienne powiadomienia, jeśli dla ogłoszenia złożono więcej ofert. Możesz zdecydować o nieprzyjmowaniu tych powiadomień poprzez usunięcie zaznaczenia z pola wyboru.
</div>
</div>
</td>
</tr>
</table>
</div>
<script>
var kj_ads_queryParam = {"adsenseQuery":"Przytulne, 2 pokojowe, 35m, Ruczaj, Babińskiego","afsChannels":"r_Krakow,Total,c_housing,l_vip","locale":"pl-PL","adsenseClientAFS":"gumtree-pl-vip","type":"google","afcChannels":"r_Krakow,Total,c_housing","pageNum":"1","totalAds":3,"isGoogleTest":false,"adSafe":false,"adsenseClientAFC":"","invocationType":"afs","afcClientId":"ca-gumtree-pl_js"};
var kj_ads_dispParam = {"layOut":"","mediaplexDomain":"http://mktg.gumtree.pl/cm/bk/","dispType":"vip","trackType":"mplx","mplxUrl":"9860-56167-3840-27?LocClass-AdSenseClick=1&amp;mpuid=;;;;;;;r_Krakow,c_housing;;1406784571895"};
kj_ads_dispParam.imgPlaceHolderIconUrl = 'http://pic.classistatic.com/image/pics/classifieds/pl-PL/image_placeholder_gt1.gif';
kj_ads_dispParam.adSenseTitle = 'Linki sponsorowane';
</script>
<script>
Kj_ad.init(kj_ads_queryParam,kj_ads_dispParam);
</script>
<style>
#persistInput.storeMachId {behavior:url(#default#userData);}
</style>
<form id="persistForm">
<input type="hidden" class="storeMachId" id="persistInput"/>
</form>
<script>
Kj.initMachineId({isProduction:true,cookiePath:'http://include.classistatic.com/include/e884/c3js/classifieds/rel1/FLASH/'});
</script>
<!-- CC JS Includes -->
<script type="text/javascript" charset="UTF-8">
//start-CC JS
$().ready(function(){$(".s2f").kjmenu_makeMenu({data:"\0030\003Podziel się na Facebooku\0030\004"+"\0031\003Podziel się na Twitterze\0031\004"+"\0033\003Wyślij znajomym\0033",OnSelect:function(mitem){switch(mitem.value){case'0':window.open('http://www.facebook.com/share.php?src=bm&u=http%3A%2F%2Fgumtree.pl%2Fc-ViewAd%3FAdId%3D607878925%26utm_source%3DFacebook%26utm_medium%3DSocial%252BMedia%26utm_campaign%3DPost%252BTo%252BFacebook&t=Przytulne%2C%202%20pokojowe%2C%2035m%2C%20Ruczaj%2C%20Babi%C5%84skiego%20-%20Gumtree%20Polska&v=3');break;case'1':window.open('http://twitter.com/?status=http%3A%2F%2Fgumtree.pl%2Fc-ViewAd%3FAdId%3D607878925');break;case'3':location.href='/c-SendToFriend?AdId=607878925';break;}}});});var googletag=googletag||{};googletag.cmd=googletag.cmd||[];(function(){var gads=document.createElement('script');gads.async=true;gads.type='text/javascript';var useSSL='https:'==document.location.protocol;gads.src=(useSSL?'https:':'http:')+'//www.googletagservices.com/tag/js/gpt.js';var node=document.getElementsByTagName('script')[0];node.parentNode.insertBefore(gads,node);})();$(document).ready(function(){pageURL=window.location.href;curLOC=$("#searchLoc_name").text()||"";curLOC=curLOC.replace(/\W+/g,'_');googletag.cmd.push(function(){googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci_VIP/mieszkania_i_domy_do_wynaj_cia',[300,250],'div-gpt-ad-1318934199048-0').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","Przytulne,2,pokojowe,35m,Ruczaj,Babi,skiego").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci_VIP/mieszkania_i_domy_do_wynaj_cia',[300,250],'div-gpt-ad-1318934199048-1').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","Przytulne,2,pokojowe,35m,Ruczaj,Babi,skiego").setTargeting("dc_ref",pageURL);googletag.defineSlot('/7162/Gumtree_PL/Nieruchomo_ci_VIP/mieszkania_i_domy_do_wynaj_cia',[[728,90],[750,200]],'div-gpt-ad-vip-topbanner').addService(googletag.pubads()).setTargeting("loc",curLOC).setTargeting("kw","Przytulne,2,pokojowe,35m,Ruczaj,Babi,skiego").setTargeting("dc_ref",pageURL);googletag.enableServices();});googletag.cmd.push(function(){googletag.display('div-gpt-ad-1318934199048-0');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-1318934199048-1');});googletag.cmd.push(function(){googletag.display('div-gpt-ad-vip-topbanner');});});setTimeout(function(){var a=document.createElement("script");var b=document.getElementsByTagName("script")[0];a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0017/0492.js?"+Math.floor(new Date().getTime()/3600000);a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)},1);_atrk_opts={atrk_acct:"wS4fj1a4ZP00g+",domain:"gumtree.pl",dynamic:true};(function(){var as=document.createElement('script');as.type='text/javascript';as.async=true;as.src="https://d31qbv1cthcecs.cloudfront.net/atrk.js";var s=document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as,s);})();
//end -CC JS
//start-TAIL JS
Kj.initGA({isGaSiteTrackerId:true,isGaTrackerId:false});$(document).ready(function(){$('.mainTabs a[href$="c-SelectCategory"]').bind('click',function(){Kj.Ga.trackEventsinGA({category:'Header_PostAdTab',action:'Header_PostAdTab_clicked',opt_label:undefined,track_on_area_level:true});});});var catdata="\0030\003Wszystkie kategorie\0030\0031\0030\004\0030-0\003Nieruchomości\0032\0031\0031\0040-0\0030-0_0\003Wszystkie Nieruchomości\0032\0031\0030\0040-0\0030-0_1\003pokoje do wynajęcia\0039000\0031\0031\0040-0\0030-0_2\003mieszkania i domy do wynajęcia\0039008\0031\0031\0040-0\0030-0_3\003mieszkania i domy - sprzedam i kupię\0039073\0031\0031\0040-0\0030-0_4\003działki\0039194\0031\0031\0040-0\0030-0_5\003krótki termin i noclegi\0039074\0031\0031\0040-0\0030-0_6\003kwatery i domki letniskowe\0039193\0031\0031\0040-0\0030-0_7\003lokal i biuro\0039072\0031\0031\0040-0\0030-0_8\003parking i garaż\0039071\0031\0031\004\0030-1\003Motoryzacja\0035\0031\0031\0040-1\0030-1_0\003Wszystkie Motoryzacja\0035\0031\0030\0040-1\0030-1_1\003samochody osobowe\0039026\0031\0031\0040-1\0030-1_2\003samochody dostawcze\0039027\0031\0031\0040-1\0030-1_3\003motocykle i skutery\0039028\0031\0031\0040-1\0030-1_4\003ciągniki i maszyny rolnicze\0039154\0031\0031\0040-1\0030-1_5\003przyczepy i naczepy\0039155\0031\0031\0040-1\0030-1_6\003części i akcesoria\0039029\0031\0031\004\0030-2\003Łodzie i Pojazdy wodne\0039218\0031\0031\0040-2\0030-2_0\003Wszystkie Łodzie i Pojazdy wodne\0039218\0031\0030\0040-2\0030-2_1\003motorówki\0039219\0031\0031\0040-2\0030-2_2\003skutery wodne\0039222\0031\0031\0040-2\0030-2_3\003żaglówki\0039221\0031\0031\0040-2\0030-2_4\003kajaki i pontony\0039220\0031\0031\0040-2\0030-2_5\003silniki do łodzi\0039223\0031\0031\0040-2\0030-2_6\003akcesoria do łodzi\0039224\0031\0031\0040-2\0030-2_7\003inne pojazdy wodne\0039225\0031\0031\0040-2\0030-2_8\003łodzie wiosłowe\0039226\0031\0031\004\0030-3\003Sprzedam\0034\0031\0031\0040-3\0030-3_0\003Wszystkie Sprzedam\0034\0031\0030\0040-3\0030-3_1\003AGD\0039366\0031\0031\0040-3\0030-3_2\003antyki i kolekcje\0039351\0031\0031\0040-3\0030-3_3\003meble\0039376\0031\0031\0040-3\0030-3_4\003narzędzia i materiały budowlane\0039384\0031\0031\0040-3\0030-3_5\003ogród\0039398\0031\0031\0040-3\0030-3_6\003produkty żywnościowe\0039407\0031\0031\0040-3\0030-3_7\003wyposażenie wnętrz\0039408\0031\0031\0040-3\0030-3_8\003zdrowie\0039418\0031\0031\0040-3\0030-3_9\003sprzedam inne\0039023\0031\0031\004\0030-4\003Elektronika\0039237\0031\0031\0040-4\0030-4_0\003Wszystkie Elektronika\0039237\0031\0030\0040-4\0030-4_1\003audio i hi-fi\0039260\0031\0031\0040-4\0030-4_2\003cesje\0039353\0031\0031\0040-4\0030-4_3\003fotografia i video\0039281\0031\0031\0040-4\0030-4_4\003gry video i konsole\0039265\0031\0031\0040-4\0030-4_5\003komputery i software\0039238\0031\0031\0040-4\0030-4_6\003radiokomunikacja\0039352\0031\0031\0040-4\0030-4_7\003tablety i bookreadery\0039259\0031\0031\0040-4\0030-4_8\003telefony i akcesoria\0039247\0031\0031\0040-4\0030-4_9\003telewizory i odtwarzacze\0039276\0031\0031\0040-4\0030-4_10\003elektronika inne\0039286\0031\0031\004\0030-5\003Dla Dziecka\0039459\0031\0031\0040-5\0030-5_0\003Wszystkie Dla Dziecka\0039459\0031\0030\0040-5\0030-5_1\003artykuły szkolne\0039468\0031\0031\0040-5\0030-5_2\003bezpieczeństwo i zdrowie dziecka\0039460\0031\0031\0040-5\0030-5_3\003buty dla dzieci\0039461\0031\0031\0040-5\0030-5_4\003chrzciny, komunie, imprezy\0039469\0031\0031\0040-5\0030-5_5\003ciąża i karmienie\0039464\0031\0031\0040-5\0030-5_6\003foteliki - nosidełka\0039462\0031\0031\0040-5\0030-5_7\003kąpiel i zdrowie\0039470\0031\0031\0040-5\0030-5_8\003kojce i chodziki\0039471\0031\0031\0040-5\0030-5_9\003meble i wystrój pokoju\0039463\0031\0031\0040-5\0030-5_10\003rowerki i inne pojazdy\0039472\0031\0031\0040-5\0030-5_11\003odzież dziecięca\0039465\0031\0031\0040-5\0030-5_12\003wózki dla dzieci\0039466\0031\0031\0040-5\0030-5_13\003zabawki\0039467\0031\0031\0040-5\0030-5_14\003inne dla dziecka\0039489\0031\0031\004\0030-6\003Sport i Rozrywka\0039490\0031\0031\0040-6\0030-6_0\003Wszystkie Sport i Rozrywka\0039490\0031\0030\0040-6\0030-6_1\003bilety\0039491\0031\0031\0040-6\0030-6_2\003instrumenty i akcesoria muzyczne\0039496\0031\0031\0040-6\0030-6_3\003komiksy i czasopisma\0039497\0031\0031\0040-6\0030-6_4\003książki\0039498\0031\0031\0040-6\0030-6_5\003CD, kasety i płyty\0039514\0031\0031\0040-6\0030-6_6\003filmy i DVD\0039513\0031\0031\0040-6\0030-6_7\003gry planszowe i puzzle\0039515\0031\0031\0040-6\0030-6_8\003sport\0039519\0031\0031\0040-6\0030-6_9\003sprzęt turystyczny\0039531\0031\0031\004\0030-7\003Zwierzaki\0039124\0031\0031\0040-7\0030-7_0\003Wszystkie Zwierzaki\0039124\0031\0030\0040-7\0030-7_1\003psy i szczenięta\0039131\0031\0031\0040-7\0030-7_2\003koty i kocięta\0039125\0031\0031\0040-7\0030-7_3\003inne zwierzaki\0039126\0031\0031\0040-7\0030-7_4\003zgubiono lub znaleziono\0039128\0031\0031\0040-7\0030-7_5\003akcesoria dla zwierząt\0039129\0031\0031\0040-7\0030-7_6\003usługi dla zwierząt\0039130\0031\0031\004\0030-8\003Społeczność\0036\0031\0031\0040-8\0030-8_0\003Wszystkie Społeczność\0036\0031\0030\0040-8\0030-8_1\003drobne pytania i hobby\0039030\0031\0031\0040-8\0030-8_2\003sport, taniec i partnerzy do gry\0039032\0031\0031\0040-8\0030-8_3\003zespoły i muzycy\0039033\0031\0031\0040-8\0030-8_4\003wolontariat\0039227\0031\0031\0040-8\0030-8_5\003wydarzenia lokalne\0039228\0031\0031\0040-8\0030-8_6\003wymiana umiejętności\0039035\0031\0031\0040-8\0030-8_7\003zgubiono lub znaleziono\0039036\0031\0031\0040-8\0030-8_8\003przejazdy\0039037\0031\0031\0040-8\0030-8_9\003podróże\0039038\0031\0031\0040-8\0030-8_10\003dziękuję\0039039\0031\0031\0040-8\0030-8_11\003wyznania\0039084\0031\0031\0040-8\0030-8_12\003szukam starych przyjaciół\0039132\0031\0031\004\0030-9\003Oferty Pracy\0038\0031\0031\0040-9\0030-9_0\003Wszystkie Oferty Pracy\0038\0031\0030\0040-9\0030-9_1\003bar, restauracja i gastronomia\0039056\0031\0031\0040-9\0030-9_2\003biuro i administracja\0039052\0031\0031\0040-9\0030-9_3\003praca na budowie i pracownicy fizyczni\0039142\0031\0031\0040-9\0030-9_4\003fachowcy\0039203\0031\0031\0040-9\0030-9_5\003finanse i księgowość\0039050\0031\0031\0040-9\0030-9_6\003grafika i web design\0039140\0031\0031\0040-9\0030-9_7\003hostessy, modele i aktorzy\0039141\0031\0031\0040-9\0030-9_8\003hr, kadry i rekrutacja\0039053\0031\0031\0040-9\0030-9_9\003inżynierowie, technicy i architekci\0039094\0031\0031\0040-9\0030-9_10\003kierowcy i kurierzy\0039097\0031\0031\0040-9\0030-9_11\003kontrola i inwentaryzacja\0039208\0031\0031\0040-9\0030-9_12\003krawiectwo i moda\0039204\0031\0031\0040-9\0030-9_13\003marketing, media i pr\0039048\0031\0031\0040-9\0030-9_14\003praca typu mlm\0039532\0031\0031\0040-9\0030-9_15\003nauczyciele i edukacja\0039060\0031\0031\0040-9\0030-9_16\003ochrona\0039200\0031\0031\0040-9\0030-9_17\003opiekunki i nianie\0039059\0031\0031\0040-9\0030-9_18\003pielęgnacja i uroda\0039054\0031\0031\0040-9\0030-9_19\003praca dla studentów\0039206\0031\0031\0040-9\0030-9_20\003praca w hotelu\0039058\0031\0031\0040-9\0030-9_21\003prawo i prokuratura\0039049\0031\0031\0040-9\0030-9_22\003programiści, informatyka i internet\0039005\0031\0031\0040-9\0030-9_23\003służba zdrowia i farmacja\0039055\0031\0031\0040-9\0030-9_24\003spedycja\0039205\0031\0031\0040-9\0030-9_25\003sport i fitness\0039202\0031\0031\0040-9\0030-9_26\003sprzątanie i pomoc domowa\0039138\0031\0031\0040-9\0030-9_27\003sprzedaż, handel i praca w sklepie\0039061\0031\0031\0040-9\0030-9_28\003telemarketing i call center\0039098\0031\0031\0040-9\0030-9_29\003turystyka\0039207\0031\0031\0040-9\0030-9_30\003ulotki\0039201\0031\0031\0040-9\0030-9_31\003weterynaria i rolnictwo\0039095\0031\0031\0040-9\0030-9_32\003video i fotografia\0039212\0031\0031\0040-9\0030-9_33\003praca inne\0039099\0031\0031\004\0030-10\003Szukający Zatrudnienia\0039290\0031\0031\0040-10\0030-10_0\003Wszystkie Szukający Zatrudnienia\0039290\0031\0030\0040-10\0030-10_1\003gastronomia\0039291\0031\0031\0040-10\0030-10_2\003biuro i administracja\0039292\0031\0031\0040-10\0030-10_3\003pracownicy fizyczni\0039293\0031\0031\0040-10\0030-10_4\003specjaliści i technicy\0039294\0031\0031\0040-10\0030-10_5\003kierowcy i kurierzy\0039300\0031\0031\0040-10\0030-10_6\003marketing i reklama\0039304\0031\0031\0040-10\0030-10_7\003opiekunki i edukacja\0039305\0031\0031\0040-10\0030-10_8\003ochrona\0039306\0031\0031\0040-10\0030-10_9\003pielęgnacja i uroda\0039308\0031\0031\0040-10\0030-10_10\003sprzedaż i praca w sklepie\0039311\0031\0031\0040-10\0030-10_11\003szukam pracy studenckiej\0039309\0031\0031\0040-10\0030-10_12\003turystyka\0039312\0031\0031\0040-10\0030-10_13\003pozostałe\0039313\0031\0031\004\0030-11\003Usługi\0039\0031\0031\0040-11\0030-11_0\003Wszystkie Usługi\0039\0031\0030\0040-11\0030-11_1\003biura podróży\0039150\0031\0031\0040-11\0030-11_2\003współpraca biznesowa\0039325\0031\0031\0040-11\0030-11_3\003catering\0039554\0031\0031\0040-11\0030-11_4\003usługi finansowe\0039066\0031\0031\0040-11\0030-11_5\003fotografia i video\0039146\0031\0031\0040-11\0030-11_6\003graficy i usługi IT\0039234\0031\0031\0040-11\0030-11_7\003hurt i handel\0039065\0031\0031\0040-11\0030-11_8\003komputery serwis i handel\0039102\0031\0031\0040-11\0030-11_9\003usługi kurierskie\0039337\0031\0031\0040-11\0030-11_10\003nauka i edukacja\0039063\0031\0031\0040-11\0030-11_11\003mechanika i autoskup\0039145\0031\0031\0040-11\0030-11_12\003media i reklama\0039217\0031\0031\0040-11\0030-11_13\003muzycy i artyści\0039148\0031\0031\0040-11\0030-11_14\003ogrodnictwo\0039214\0031\0031\0040-11\0030-11_15\003opieka i agencje niań\0039152\0031\0031\0040-11\0030-11_16\003pielęgnacja i uroda\0039064\0031\0031\0040-11\0030-11_17\003usługi prawne\0039233\0031\0031\0040-11\0030-11_18\003przeprowadzki\0039144\0031\0031\0040-11\0030-11_19\003remont i budowa\0039101\0031\0031\0040-11\0030-11_20\003serwis i montaż\0039236\0031\0031\0040-11\0030-11_21\003sport i fitness\0039151\0031\0031\0040-11\0030-11_22\003sprzątanie\0039149\0031\0031\0040-11\0030-11_23\003śluby, wesela i przyjęcia\0039104\0031\0031\0040-11\0030-11_24\003taxi i przewozy osobowe\0039147\0031\0031\0040-11\0030-11_25\003telefony\0039341\0031\0031\0040-11\0030-11_26\003tłumaczenia i redakcja tekstu\0039216\0031\0031\0040-11\0030-11_27\003utylizacja\0039213\0031\0031\0040-11\0030-11_28\003wypożyczalnie\0039215\0031\0031\0040-11\0030-11_29\003zdrowie\0039235\0031\0031\0040-11\0030-11_30\003inne usługi\0039105\0031\0031\004\0030-12\003Moda\0039541\0031\0031\0040-12\0030-12_0\003Wszystkie Moda\0039541\0031\0030\0040-12\0030-12_1\003akcesoria i galanteria\0039542\0031\0031\0040-12\0030-12_2\003biżuteria i zegarki\0039563\0031\0031\0040-12\0030-12_3\003kosmetyki i perfumy\0039544\0031\0031\0040-12\0030-12_4\003obuwie damskie\0039596\0031\0031\0040-12\0030-12_5\003obuwie męskie\0039604\0031\0031\0040-12\0030-12_6\003odzież damska\0039565\0031\0031\0040-12\0030-12_7\003odzież męska\0039584\0031\0031\0040-12\0030-12_8\003pasmanteria\0039549\0031\0031\0040-12\0030-12_9\003torebki i torby\0039551\0031\0031\0040-12\0030-12_10\003walizki i plecaki\0039552\0031\0031\0040-12\0030-12_11\003inne ubrania\0039553\0031\0031\004";$().ready(function(){$("#searchCat").kjmenu_makeMenu({data:catdata,cssWrapperClass:'nationalSite',OnSelect:function(mitem){$("#searchCat_name").html(mitem.name+"<img border='0' src='http://pic.classistatic.com/image/pics/classifieds/spacer.gif' width='25px' height='1px'/></div>");document.frmSearchAd.CatId.value=mitem.value;$('.sfsp').remove();$('.sfasp').remove();}});});var sdata="\0030\003Polska\003202\0031\0030\004\0030-0\003Dolnośląskie\0033200007\0031\0031\0040-0\0030-0_0\003Wszystkie Dolnośląskie\0033200007\0031\0030\0040-0\0030-0_1\003Bielawa\0033200085\0031\0031\0040-0\0030-0_2\003 Bierutów\0033200435\0031\0031\0040-0\0030-0_3\003Bogatynia\0033200086\0031\0031\0040-0\0030-0_4\003 Boguszów-Gorce\0033200437\0031\0031\0040-0\0030-0_5\003Bolesławiec\0033200087\0031\0031\0040-0\0030-0_6\003 Bolków\0033200436\0031\0031\0040-0\0030-0_7\003 Brzeg Dolny\0033200438\0031\0031\0040-0\0030-0_8\003 Bystrzyca Kłodzka\0033200439\0031\0031\0040-0\0030-0_9\003 Chocianów\0033200440\0031\0031\0040-0\0030-0_10\003 Chojnów\0033200441\0031\0031\0040-0\0030-0_11\003Dzierżoniów\0033200088\0031\0031\0040-0\0030-0_12\003Głogów\0033200089\0031\0031\0040-0\0030-0_13\003Góra\0033200090\0031\0031\0040-0\0030-0_14\003 Gryfów Śląski\0033200442\0031\0031\0040-0\0030-0_15\003Jawor\0033200091\0031\0031\0040-0\0030-0_16\003 Jelcz-Laskowice\0033200443\0031\0031\0040-0\0030-0_17\003Jelenia Góra\0033200092\0031\0031\0040-0\0030-0_18\003Kamienna Góra\0033200093\0031\0031\0040-0\0030-0_19\003Karpacz\0033200094\0031\0031\0040-0\0030-0_20\003Kłodzko\0033200095\0031\0031\0040-0\0030-0_21\003 Kowary\0033200444\0031\0031\0040-0\0030-0_22\003 Kudowa-Zdrój\0033200445\0031\0031\0040-0\0030-0_23\003Legnica\0033200096\0031\0031\0040-0\0030-0_24\003Lubań\0033200097\0031\0031\0040-0\0030-0_25\003Lubin\0033200098\0031\0031\0040-0\0030-0_26\003Lwówek Śląski\0033200099\0031\0031\0040-0\0030-0_27\003Milicz\0033200100\0031\0031\0040-0\0030-0_28\003Nowa Ruda\0033200101\0031\0031\0040-0\0030-0_29\003 Oborniki Śląskie\0033200446\0031\0031\0040-0\0030-0_30\003Oława\0033200102\0031\0031\0040-0\0030-0_31\003Oleśnica\0033200103\0031\0031\0040-0\0030-0_32\003Piechowice\0033200434\0031\0031\0040-0\0030-0_33\003 Pieszyce\0033200447\0031\0031\0040-0\0030-0_34\003 Piława Górna\0033200448\0031\0031\0040-0\0030-0_35\003Polanica-Zdrój\0033200104\0031\0031\0040-0\0030-0_36\003Polkowice\0033200105\0031\0031\0040-0\0030-0_37\003 Strzegom\0033200449\0031\0031\0040-0\0030-0_38\003Strzelin\0033200107\0031\0031\0040-0\0030-0_39\003 Syców\0033200450\0031\0031\0040-0\0030-0_40\003Szklarska Poręba\0033200106\0031\0031\0040-0\0030-0_41\003Środa Śląska\0033200108\0031\0031\0040-0\0030-0_42\003Świdnica\0033200109\0031\0031\0040-0\0030-0_43\003Świebodzice\0033200110\0031\0031\0040-0\0030-0_44\003Trzebnica\0033200111\0031\0031\0040-0\0030-0_45\003Wałbrzych\0033200112\0031\0031\0040-0\0030-0_46\003Wołów\0033200113\0031\0031\0040-0\0030-0_47\003Wrocław\0033200114\0031\0031\0040-0\0030-0_48\003Ząbkowice Śląskie\0033200115\0031\0031\0040-0\0030-0_49\003Zgorzelec\0033200116\0031\0031\0040-0\0030-0_50\003 Ziębice\0033200451\0031\0031\0040-0\0030-0_51\003Złotoryja\0033200117\0031\0031\0040-0\0030-0_52\003 Żarów\0033200452\0031\0031\0040-0\0030-0_53\003 Żmigród\0033200453\0031\0031\004\0030-1\003Kujawsko - pomorskie\0033200075\0031\0031\0040-1\0030-1_0\003Wszystkie Kujawsko - pomorskie\0033200075\0031\0030\0040-1\0030-1_1\003Aleksandrów Kujawski\0033200118\0031\0031\0040-1\0030-1_2\003 Barcin\0033200454\0031\0031\0040-1\0030-1_3\003Brodnica\0033200119\0031\0031\0040-1\0030-1_4\003Bydgoszcz\0033200120\0031\0031\0040-1\0030-1_5\003Chełmno\0033200121\0031\0031\0040-1\0030-1_6\003 Chełmża\0033200455\0031\0031\0040-1\0030-1_7\003 Ciechocinek\0033200456\0031\0031\0040-1\0030-1_8\003 Gniewkowo\0033200457\0031\0031\0040-1\0030-1_9\003Golub-Dobrzyń\0033200122\0031\0031\0040-1\0030-1_10\003Grudziądz\0033200123\0031\0031\0040-1\0030-1_11\003Inowrocław\0033200124\0031\0031\0040-1\0030-1_12\003 Janikowo\0033200458\0031\0031\0040-1\0030-1_13\003 Koronowo\0033200459\0031\0031\0040-1\0030-1_14\003 Kruszwica\0033200460\0031\0031\0040-1\0030-1_15\003Lipno\0033200125\0031\0031\0040-1\0030-1_16\003Mogilno\0033200126\0031\0031\0040-1\0030-1_17\003Nakło nad Notecią\0033200127\0031\0031\0040-1\0030-1_18\003Radziejów\0033200128\0031\0031\0040-1\0030-1_19\003Rypin\0033200129\0031\0031\0040-1\0030-1_20\003Sępólno Krajeńskie\0033200130\0031\0031\0040-1\0030-1_21\003 Solec Kujawski\0033200461\0031\0031\0040-1\0030-1_22\003 Strzelno\0033200462\0031\0031\0040-1\0030-1_23\003Świecie\0033200131\0031\0031\0040-1\0030-1_24\003 Szubin\0033200463\0031\0031\0040-1\0030-1_25\003Toruń\0033200132\0031\0031\0040-1\0030-1_26\003Tuchola\0033200133\0031\0031\0040-1\0030-1_27\003Wąbrzeźno\0033200134\0031\0031\0040-1\0030-1_28\003 Więcbork\0033200464\0031\0031\0040-1\0030-1_29\003Włocławek\0033200135\0031\0031\0040-1\0030-1_30\003Żnin\0033200136\0031\0031\004\0030-2\003Lubelskie\0033200076\0031\0031\0040-2\0030-2_0\003Wszystkie Lubelskie\0033200076\0031\0030\0040-2\0030-2_1\003Bełżyce\0033200465\0031\0031\0040-2\0030-2_2\003Biała Podlaska\0033200137\0031\0031\0040-2\0030-2_3\003Biłgoraj\0033200138\0031\0031\0040-2\0030-2_4\003Chełm\0033200139\0031\0031\0040-2\0030-2_5\003Dęblin\0033200466\0031\0031\0040-2\0030-2_6\003Hrubieszów\0033200140\0031\0031\0040-2\0030-2_7\003Janów Lubelski\0033200141\0031\0031\0040-2\0030-2_8\003Krasnystaw\0033200142\0031\0031\0040-2\0030-2_9\003Kraśnik\0033200143\0031\0031\0040-2\0030-2_10\003Lubartów\0033200144\0031\0031\0040-2\0030-2_11\003Lublin\0033200145\0031\0031\0040-2\0030-2_12\003Łęczna\0033200146\0031\0031\0040-2\0030-2_13\003Łuków\0033200147\0031\0031\0040-2\0030-2_14\003Międzyrzec Podlaski\0033200467\0031\0031\0040-2\0030-2_15\003Opole Lubelskie\0033200148\0031\0031\0040-2\0030-2_16\003Parczew\0033200149\0031\0031\0040-2\0030-2_17\003Poniatowa\0033200468\0031\0031\0040-2\0030-2_18\003Puławy\0033200150\0031\0031\0040-2\0030-2_19\003Radzyń Podlaski\0033200151\0031\0031\0040-2\0030-2_20\003Ryki\0033200152\0031\0031\0040-2\0030-2_21\003Świdnik\0033200153\0031\0031\0040-2\0030-2_22\003Terespol\0033200469\0031\0031\0040-2\0030-2_23\003Tomaszów Lubelski\0033200154\0031\0031\0040-2\0030-2_24\003Włodawa\0033200155\0031\0031\0040-2\0030-2_25\003Zamość\0033200156\0031\0031\004\0030-3\003Lubuskie\0033200077\0031\0031\0040-3\0030-3_0\003Wszystkie Lubuskie\0033200077\0031\0030\0040-3\0030-3_1\003Drezdenko\0033200158\0031\0031\0040-3\0030-3_2\003Gorzów Wielkopolski\0033200157\0031\0031\0040-3\0030-3_3\003Gubin\0033200159\0031\0031\0040-3\0030-3_4\003 Kostrzyn nad Odrą\0033200470\0031\0031\0040-3\0030-3_5\003 Kożuchów\0033200471\0031\0031\0040-3\0030-3_6\003Krosno Odrzańskie\0033200160\0031\0031\0040-3\0030-3_7\003Lubsko\0033200161\0031\0031\0040-3\0030-3_8\003Międzyrzecz\0033200162\0031\0031\0040-3\0030-3_9\003Nowa Sól\0033200163\0031\0031\0040-3\0030-3_10\003 Rzepin\0033200472\0031\0031\0040-3\0030-3_11\003sulechów\0033200166\0031\0031\0040-3\0030-3_12\003Słubice\0033200164\0031\0031\0040-3\0030-3_13\003Strzelce Krajeńskie\0033200165\0031\0031\0040-3\0030-3_14\003 Skwierzyna\0033200473\0031\0031\0040-3\0030-3_15\003Sulęcin\0033200167\0031\0031\0040-3\0030-3_16\003Szprotawa\0033200168\0031\0031\0040-3\0030-3_17\003Świebodzin\0033200169\0031\0031\0040-3\0030-3_18\003 Witnica\0033200474\0031\0031\0040-3\0030-3_19\003Wschowa\0033200170\0031\0031\0040-3\0030-3_20\003Zielona Góra\0033200171\0031\0031\0040-3\0030-3_21\003Żagań\0033200172\0031\0031\0040-3\0030-3_22\003Żary\0033200173\0031\0031\004\0030-4\003Łódzkie\0033200004\0031\0031\0040-4\0030-4_0\003Wszystkie Łódzkie\0033200004\0031\0030\0040-4\0030-4_1\003Aleksandrów Łódzki\0033200174\0031\0031\0040-4\0030-4_2\003Bełchatów\0033200175\0031\0031\0040-4\0030-4_3\003Brzeziny\0033200176\0031\0031\0040-4\0030-4_4\003Głowno\0033200177\0031\0031\0040-4\0030-4_5\003 Koluszki\0033200475\0031\0031\0040-4\0030-4_6\003Konstantynów Łódzki\0033200178\0031\0031\0040-4\0030-4_7\003Kutno\0033200179\0031\0031\0040-4\0030-4_8\003Łask\0033200180\0031\0031\0040-4\0030-4_9\003Łęczyca\0033200181\0031\0031\0040-4\0030-4_10\003Łowicz\0033200182\0031\0031\0040-4\0030-4_11\003Łódź\0033200183\0031\0031\0040-4\0030-4_12\003Opoczno\0033200184\0031\0031\0040-4\0030-4_13\003Ozorków\0033200185\0031\0031\0040-4\0030-4_14\003Pabianice\0033200186\0031\0031\0040-4\0030-4_15\003Pajęczno\0033200187\0031\0031\0040-4\0030-4_16\003Piotrków Trybunalski\0033200188\0031\0031\0040-4\0030-4_17\003Poddębice\0033200189\0031\0031\0040-4\0030-4_18\003Radomsko\0033200190\0031\0031\0040-4\0030-4_19\003Rawa Mazowiecka\0033200191\0031\0031\0040-4\0030-4_20\003Sieradz\0033200192\0031\0031\0040-4\0030-4_21\003Skierniewice\0033200193\0031\0031\0040-4\0030-4_22\003 Tuszyn\0033200476\0031\0031\0040-4\0030-4_23\003Tomaszów Mazowiecki\0033200194\0031\0031\0040-4\0030-4_24\003Wieluń\0033200195\0031\0031\0040-4\0030-4_25\003Wieruszów\0033200196\0031\0031\0040-4\0030-4_26\003Zduńska Wola\0033200197\0031\0031\0040-4\0030-4_27\003 Zelów\0033200477\0031\0031\0040-4\0030-4_28\003Zgierz\0033200198\0031\0031\0040-4\0030-4_29\003 Żychlin\0033200478\0031\0031\004\0030-5\003Małopolskie\0033200003\0031\0031\0040-5\0030-5_0\003Wszystkie Małopolskie\0033200003\0031\0030\0040-5\0030-5_1\003Andrychów\0033200199\0031\0031\0040-5\0030-5_2\003Bochnia\0033200200\0031\0031\0040-5\0030-5_3\003Brzesko\0033200201\0031\0031\0040-5\0030-5_4\003Brzeszcze\0033200479\0031\0031\0040-5\0030-5_5\003Bukowina Tatrzańska\0033200202\0031\0031\0040-5\0030-5_6\003Bukowno\0033200480\0031\0031\0040-5\0030-5_7\003Chełmek\0033200481\0031\0031\0040-5\0030-5_8\003Chrzanów\0033200203\0031\0031\0040-5\0030-5_9\003Dąbrowa Tarnowska\0033200204\0031\0031\0040-5\0030-5_10\003Gorlice\0033200205\0031\0031\0040-5\0030-5_11\003Kęty\0033200206\0031\0031\0040-5\0030-5_12\003Kościelisko\0033200207\0031\0031\0040-5\0030-5_13\003Kraków\0033200208\0031\0031\0040-5\0030-5_14\003Krościenko nad Dunajcem\0033200491\0031\0031\0040-5\0030-5_15\003Krynica-Zdrój\0033200209\0031\0031\0040-5\0030-5_16\003Krzeszowice\0033200482\0031\0031\0040-5\0030-5_17\003Libiąż\0033200483\0031\0031\0040-5\0030-5_18\003Limanowa\0033200210\0031\0031\0040-5\0030-5_19\003Miechów\0033200211\0031\0031\0040-5\0030-5_20\003Mszana Dolna\0033200484\0031\0031\0040-5\0030-5_21\003Myślenice\0033200212\0031\0031\0040-5\0030-5_22\003Niepołomice\0033200485\0031\0031\0040-5\0030-5_23\003Nowy Sącz\0033200213\0031\0031\0040-5\0030-5_24\003Nowy Targ\0033200214\0031\0031\0040-5\0030-5_25\003Olkusz\0033200215\0031\0031\0040-5\0030-5_26\003Oświęcim\0033200216\0031\0031\0040-5\0030-5_27\003Piwniczna-Zdrój\0033200486\0031\0031\0040-5\0030-5_28\003Proszowice\0033200217\0031\0031\0040-5\0030-5_29\003Rabka-Zdrój\0033200487\0031\0031\0040-5\0030-5_30\003Skawina\0033200218\0031\0031\0040-5\0030-5_31\003Stary Sącz\0033200488\0031\0031\0040-5\0030-5_32\003Sucha Beskidzka\0033200219\0031\0031\0040-5\0030-5_33\003Szczawnica\0033200220\0031\0031\0040-5\0030-5_34\003Tarnów\0033200221\0031\0031\0040-5\0030-5_35\003Trzebinia\0033200222\0031\0031\0040-5\0030-5_36\003Tuchów\0033200489\0031\0031\0040-5\0030-5_37\003Wadowice\0033200223\0031\0031\0040-5\0030-5_38\003Wieliczka\0033200224\0031\0031\0040-5\0030-5_39\003Wolbrom\0033200490\0031\0031\0040-5\0030-5_40\003Zakopane\0033200225\0031\0031\004\0030-6\003Mazowieckie\0033200001\0031\0031\0040-6\0030-6_0\003Wszystkie Mazowieckie\0033200001\0031\0030\0040-6\0030-6_1\003Warszawa\0033200008\0031\0031\0040-6\0030-6_2\003Północne powiaty\0033200027\0031\0031\0040-6\0030-6_3\003Pn - wsch powiaty\0033200036\0031\0031\0040-6\0030-6_4\003Pn - zach powiaty\0033200041\0031\0031\0040-6\0030-6_5\003Południowe powiaty\0033200042\0031\0031\0040-6\0030-6_6\003Pd - wsch powiaty\0033200043\0031\0031\0040-6\0030-6_7\003Pd - zach powiaty\0033200044\0031\0031\0040-6\0030-6_8\003Wschodnie powiaty\0033200045\0031\0031\0040-6\0030-6_9\003Zachodnie powiaty\0033200046\0031\0031\004\0030-7\003Opolskie\0033200078\0031\0031\0040-7\0030-7_0\003Wszystkie Opolskie\0033200078\0031\0030\0040-7\0030-7_1\003Brzeg\0033200226\0031\0031\0040-7\0030-7_2\003Głubczyce\0033200227\0031\0031\0040-7\0030-7_3\003Grodków\0033200526\0031\0031\0040-7\0030-7_4\003Kędzierzyn-Koźle\0033200228\0031\0031\0040-7\0030-7_5\003Kluczbork\0033200229\0031\0031\0040-7\0030-7_6\003Krapkowice\0033200230\0031\0031\0040-7\0030-7_7\003Namysłów\0033200231\0031\0031\0040-7\0030-7_8\003Niemodlin\0033200527\0031\0031\0040-7\0030-7_9\003Nysa\0033200232\0031\0031\0040-7\0030-7_10\003Olesno\0033200233\0031\0031\0040-7\0030-7_11\003Opole\0033200234\0031\0031\0040-7\0030-7_12\003Ozimek\0033200528\0031\0031\0040-7\0030-7_13\003Paczków\0033200529\0031\0031\0040-7\0030-7_14\003Praszka\0033200530\0031\0031\0040-7\0030-7_15\003Prudnik\0033200235\0031\0031\0040-7\0030-7_16\003Strzelce Opolskie\0033200236\0031\0031\0040-7\0030-7_17\003Zawadzkie\0033200531\0031\0031\0040-7\0030-7_18\003Zdzieszowice\0033200532\0031\0031\004\0030-8\003Podkarpackie\0033200079\0031\0031\0040-8\0030-8_0\003Wszystkie Podkarpackie\0033200079\0031\0030\0040-8\0030-8_1\003Brzozów\0033200237\0031\0031\0040-8\0030-8_2\003Dębica\0033200238\0031\0031\0040-8\0030-8_3\003Jarosław\0033200239\0031\0031\0040-8\0030-8_4\003Jasło\0033200240\0031\0031\0040-8\0030-8_5\003Kolbuszowa\0033200241\0031\0031\0040-8\0030-8_6\003Krosno\0033200242\0031\0031\0040-8\0030-8_7\003Lesko\0033200243\0031\0031\0040-8\0030-8_8\003Leżajsk\0033200244\0031\0031\0040-8\0030-8_9\003Lubaczów\0033200245\0031\0031\0040-8\0030-8_10\003Łańcut\0033200246\0031\0031\0040-8\0030-8_11\003Mielec\0033200247\0031\0031\0040-8\0030-8_12\003Nisko\0033200248\0031\0031\0040-8\0030-8_13\003Nowa Dęba\0033200533\0031\0031\0040-8\0030-8_14\003Przemyśl\0033200249\0031\0031\0040-8\0030-8_15\003Przeworsk\0033200250\0031\0031\0040-8\0030-8_16\003Ropczyce\0033200251\0031\0031\0040-8\0030-8_17\003Rzeszów\0033200252\0031\0031\0040-8\0030-8_18\003Sanok\0033200253\0031\0031\0040-8\0030-8_19\003Sędziszów Małopolski\0033200534\0031\0031\0040-8\0030-8_20\003Stalowa Wola\0033200254\0031\0031\0040-8\0030-8_21\003Strzyżów\0033200255\0031\0031\0040-8\0030-8_22\003Tarnobrzeg\0033200256\0031\0031\0040-8\0030-8_23\003Ustrzyki Dolne\0033200257\0031\0031\004\0030-9\003Podlaskie\0033200080\0031\0031\0040-9\0030-9_0\003Wszystkie Podlaskie\0033200080\0031\0030\0040-9\0030-9_1\003Augustów\0033200258\0031\0031\0040-9\0030-9_2\003Białystok\0033200259\0031\0031\0040-9\0030-9_3\003Bielsk Podlaski\0033200260\0031\0031\0040-9\0030-9_4\003 Czarna Białostocka\0033200535\0031\0031\0040-9\0030-9_5\003 Dąbrowa Białostocka\0033200536\0031\0031\0040-9\0030-9_6\003Grajewo\0033200261\0031\0031\0040-9\0030-9_7\003Hajnówka\0033200262\0031\0031\0040-9\0030-9_8\003Kolno\0033200263\0031\0031\0040-9\0030-9_9\003Łapy\0033200264\0031\0031\0040-9\0030-9_10\003Łomża\0033200265\0031\0031\0040-9\0030-9_11\003Mońki\0033200266\0031\0031\0040-9\0030-9_12\003Sejny\0033200267\0031\0031\0040-9\0030-9_13\003Siemiatycze\0033200268\0031\0031\0040-9\0030-9_14\003Sokółka\0033200269\0031\0031\0040-9\0030-9_15\003Suwałki\0033200270\0031\0031\0040-9\0030-9_16\003 Wasilków\0033200537\0031\0031\0040-9\0030-9_17\003Wysokie Mazowieckie\0033200271\0031\0031\0040-9\0030-9_18\003Zambrów\0033200272\0031\0031\004\0030-10\003Pomorskie\0033200005\0031\0031\0040-10\0030-10_0\003Wszystkie Pomorskie\0033200005\0031\0030\0040-10\0030-10_1\003Bytów\0033200407\0031\0031\0040-10\0030-10_2\003Chojnice\0033200408\0031\0031\0040-10\0030-10_3\003Człuchów\0033200409\0031\0031\0040-10\0030-10_4\003Czersk\0033200539\0031\0031\0040-10\0030-10_5\003Gdańsk\0033200072\0031\0031\0040-10\0030-10_6\003Gdynia\0033200073\0031\0031\0040-10\0030-10_7\003Gniew\0033200543\0031\0031\0040-10\0030-10_8\003Hel\0033200410\0031\0031\0040-10\0030-10_9\003Jastarnia\0033200411\0031\0031\0040-10\0030-10_10\003Jastrzębia Góra\0033200412\0031\0031\0040-10\0030-10_11\003Kartuzy\0033200413\0031\0031\0040-10\0030-10_12\003Karwia\0033200414\0031\0031\0040-10\0030-10_13\003Kościerzyna\0033200415\0031\0031\0040-10\0030-10_14\003Krynica Morska\0033200416\0031\0031\0040-10\0030-10_15\003Kwidzyn\0033200417\0031\0031\0040-10\0030-10_16\003Łeba\0033200418\0031\0031\0040-10\0030-10_17\003Lębork\0033200419\0031\0031\0040-10\0030-10_18\003Malbork\0033200420\0031\0031\0040-10\0030-10_19\003Miastko\0033200538\0031\0031\0040-10\0030-10_20\003Nowy Dwór Gdański\0033200421\0031\0031\0040-10\0030-10_21\003Pelplin\0033200541\0031\0031\0040-10\0030-10_22\003Prabuty\0033200540\0031\0031\0040-10\0030-10_23\003Pruszcz Gdański\0033200422\0031\0031\0040-10\0030-10_24\003Puck\0033200423\0031\0031\0040-10\0030-10_25\003Reda\0033200424\0031\0031\0040-10\0030-10_26\003Rumia\0033200425\0031\0031\0040-10\0030-10_27\003Skarszewy\0033200542\0031\0031\0040-10\0030-10_28\003Słupsk\0033200426\0031\0031\0040-10\0030-10_29\003Sopot\0033200074\0031\0031\0040-10\0030-10_30\003Starogard Gdański\0033200427\0031\0031\0040-10\0030-10_31\003Stegna\0033200428\0031\0031\0040-10\0030-10_32\003Sztum\0033200429\0031\0031\0040-10\0030-10_33\003Sztutowo\0033200544\0031\0031\0040-10\0030-10_34\003Tczew\0033200430\0031\0031\0040-10\0030-10_35\003Ustka\0033200431\0031\0031\0040-10\0030-10_36\003Wejherowo\0033200432\0031\0031\0040-10\0030-10_37\003Władysławowo\0033200433\0031\0031\004\0030-11\003Śląskie\0033200002\0031\0031\0040-11\0030-11_0\003Wszystkie Śląskie\0033200002\0031\0030\0040-11\0030-11_1\003Będzin\0033200273\0031\0031\0040-11\0030-11_2\003Bielsko-Biała\0033200274\0031\0031\0040-11\0030-11_3\003Bieruń\0033200275\0031\0031\0040-11\0030-11_4\003 Blachownia\0033200545\0031\0031\0040-11\0030-11_5\003Bytom\0033200277\0031\0031\0040-11\0030-11_6\003Chorzów\0033200278\0031\0031\0040-11\0030-11_7\003Cieszyn\0033200279\0031\0031\0040-11\0030-11_8\003 Czechowice-Dziedzice\0033200546\0031\0031\0040-11\0030-11_9\003 Czeladź\0033200547\0031\0031\0040-11\0030-11_10\003 Czerwionka-Leszczyny\0033200548\0031\0031\0040-11\0030-11_11\003Częstochowa\0033200280\0031\0031\0040-11\0030-11_12\003Dąbrowa Górnicza\0033200281\0031\0031\0040-11\0030-11_13\003Gliwice\0033200282\0031\0031\0040-11\0030-11_14\003 Imielin\0033200549\0031\0031\0040-11\0030-11_15\003Jastrzębie-Zdrój\0033200283\0031\0031\0040-11\0030-11_16\003Jaworzno\0033200284\0031\0031\0040-11\0030-11_17\003 Kalety\0033200550\0031\0031\0040-11\0030-11_18\003 Knurów\0033200551\0031\0031\0040-11\0030-11_19\003Katowice\0033200285\0031\0031\0040-11\0030-11_20\003Kłobuck\0033200286\0031\0031\0040-11\0030-11_21\003 Lędziny\0033200552\0031\0031\0040-11\0030-11_22\003Lubliniec\0033200287\0031\0031\0040-11\0030-11_23\003 Łaziska Górne\0033200553\0031\0031\0040-11\0030-11_24\003Mikołów\0033200288\0031\0031\0040-11\0030-11_25\003Mysłowice\0033200289\0031\0031\0040-11\0030-11_26\003Myszków\0033200290\0031\0031\0040-11\0030-11_27\003 Orzesze\0033200554\0031\0031\0040-11\0030-11_28\003Piekary Śląskie\0033200291\0031\0031\0040-11\0030-11_29\003 Poręba\0033200555\0031\0031\0040-11\0030-11_30\003Pszczyna\0033200292\0031\0031\0040-11\0030-11_31\003 Pszów\0033200556\0031\0031\0040-11\0030-11_32\003 Pyskowice\0033200557\0031\0031\0040-11\0030-11_33\003Racibórz\0033200293\0031\0031\0040-11\0030-11_34\003 Radlin\0033200558\0031\0031\0040-11\0030-11_35\003 Radzionków\0033200559\0031\0031\0040-11\0030-11_36\003Ruda Śląska\0033200294\0031\0031\0040-11\0030-11_37\003Rybnik\0033200295\0031\0031\0040-11\0030-11_38\003 Rydułtowy\0033200560\0031\0031\0040-11\0030-11_39\003Siemianowice Śląskie\0033200296\0031\0031\0040-11\0030-11_40\003 Skoczów\0033200561\0031\0031\0040-11\0030-11_41\003Sosnowiec\0033200297\0031\0031\0040-11\0030-11_42\003Świętochłowice\0033200298\0031\0031\0040-11\0030-11_43\003Szczyrk\0033200299\0031\0031\0040-11\0030-11_44\003Tarnowskie Góry\0033200300\0031\0031\0040-11\0030-11_45\003Tychy\0033200301\0031\0031\0040-11\0030-11_46\003 Ustroń\0033200562\0031\0031\0040-11\0030-11_47\003Wisła\0033200302\0031\0031\0040-11\0030-11_48\003Wodzisław Śląski\0033200303\0031\0031\0040-11\0030-11_49\003 Wojkowice\0033200563\0031\0031\0040-11\0030-11_50\003Zabrze\0033200304\0031\0031\0040-11\0030-11_51\003Zawiercie\0033200305\0031\0031\0040-11\0030-11_52\003Żory\0033200306\0031\0031\0040-11\0030-11_53\003Żywiec\0033200307\0031\0031\004\0030-12\003Świętokrzyskie\0033200082\0031\0031\0040-12\0030-12_0\003Wszystkie Świętokrzyskie\0033200082\0031\0030\0040-12\0030-12_1\003Busko-Zdrój\0033200308\0031\0031\0040-12\0030-12_2\003Jędrzejów\0033200309\0031\0031\0040-12\0030-12_3\003Kazimierza Wielka\0033200310\0031\0031\0040-12\0030-12_4\003Kielce\0033200311\0031\0031\0040-12\0030-12_5\003Końskie\0033200312\0031\0031\0040-12\0030-12_6\003Opatów\0033200313\0031\0031\0040-12\0030-12_7\003Ostrowiec Świętokrzyski\0033200314\0031\0031\0040-12\0030-12_8\003Pińczów\0033200315\0031\0031\0040-12\0030-12_9\003Połaniec\0033200564\0031\0031\0040-12\0030-12_10\003Sandomierz\0033200316\0031\0031\0040-12\0030-12_11\003Skarżysko-Kamienna\0033200317\0031\0031\0040-12\0030-12_12\003Starachowice\0033200318\0031\0031\0040-12\0030-12_13\003Staszów\0033200319\0031\0031\0040-12\0030-12_14\003Suchedniów\0033200565\0031\0031\0040-12\0030-12_15\003Włoszczowa\0033200320\0031\0031\004\0030-13\003Warmińsko-mazurskie\0033200083\0031\0031\0040-13\0030-13_0\003Wszystkie Warmińsko-mazurskie\0033200083\0031\0030\0040-13\0030-13_1\003Bartoszyce\0033200321\0031\0031\0040-13\0030-13_2\003Biskupiec\0033200322\0031\0031\0040-13\0030-13_3\003Braniewo\0033200323\0031\0031\0040-13\0030-13_4\003Dobre Miasto\0033200324\0031\0031\0040-13\0030-13_5\003Działdowo\0033200325\0031\0031\0040-13\0030-13_6\003Elbląg\0033200326\0031\0031\0040-13\0030-13_7\003Ełk\0033200327\0031\0031\0040-13\0030-13_8\003Giżycko\0033200328\0031\0031\0040-13\0030-13_9\003Gołdap\0033200329\0031\0031\0040-13\0030-13_10\003Iława\0033200330\0031\0031\0040-13\0030-13_11\003Kętrzyn\0033200331\0031\0031\0040-13\0030-13_12\003Lidzbark Warmiński\0033200332\0031\0031\0040-13\0030-13_13\003 Lubawa\0033200566\0031\0031\0040-13\0030-13_14\003Mikołajki\0033200333\0031\0031\0040-13\0030-13_15\003 Morąg\0033200567\0031\0031\0040-13\0030-13_16\003Mrągowo\0033200334\0031\0031\0040-13\0030-13_17\003Nidzica\0033200335\0031\0031\0040-13\0030-13_18\003Nowe Miasto Lubawskie\0033200336\0031\0031\0040-13\0030-13_19\003Olecko\0033200337\0031\0031\0040-13\0030-13_20\003Olsztyn\0033200338\0031\0031\0040-13\0030-13_21\003 Olsztynek\0033200568\0031\0031\0040-13\0030-13_22\003 Orneta\0033200569\0031\0031\0040-13\0030-13_23\003Ostróda\0033200339\0031\0031\0040-13\0030-13_24\003 Pasłęk\0033200570\0031\0031\0040-13\0030-13_25\003Pisz\0033200340\0031\0031\0040-13\0030-13_26\003Szczytno\0033200341\0031\0031\0040-13\0030-13_27\003Węgorzewo\0033200342\0031\0031\004\0030-14\003Wielkopolskie\0033200006\0031\0031\0040-14\0030-14_0\003Wszystkie Wielkopolskie\0033200006\0031\0030\0040-14\0030-14_1\003Chodzież\0033200343\0031\0031\0040-14\0030-14_2\003Czarnków\0033200344\0031\0031\0040-14\0030-14_3\003Gniezno\0033200345\0031\0031\0040-14\0030-14_4\003Gostyń\0033200346\0031\0031\0040-14\0030-14_5\003Grodzisk Wielkopolski\0033200347\0031\0031\0040-14\0030-14_6\003Jarocin\0033200348\0031\0031\0040-14\0030-14_7\003Jastrowie\0033200571\0031\0031\0040-14\0030-14_8\003Kalisz\0033200349\0031\0031\0040-14\0030-14_9\003Kępno\0033200350\0031\0031\0040-14\0030-14_10\003Koło\0033200351\0031\0031\0040-14\0030-14_11\003Konin\0033200352\0031\0031\0040-14\0030-14_12\003Kostrzyn\0033200572\0031\0031\0040-14\0030-14_13\003Kościan\0033200353\0031\0031\0040-14\0030-14_14\003Kórnik\0033200573\0031\0031\0040-14\0030-14_15\003Krotoszyn\0033200354\0031\0031\0040-14\0030-14_16\003Leszno\0033200355\0031\0031\0040-14\0030-14_17\003Luboń\0033200356\0031\0031\0040-14\0030-14_18\003Międzychód\0033200357\0031\0031\0040-14\0030-14_19\003Mosina\0033200358\0031\0031\0040-14\0030-14_20\003Murowana Goślina\0033200359\0031\0031\0040-14\0030-14_21\003Nowy Tomyśl\0033200360\0031\0031\0040-14\0030-14_22\003Oborniki\0033200361\0031\0031\0040-14\0030-14_23\003Opalenica\0033200574\0031\0031\0040-14\0030-14_24\003Ostrów Wielkopolski\0033200362\0031\0031\0040-14\0030-14_25\003Ostrzeszów\0033200363\0031\0031\0040-14\0030-14_26\003Piła\0033200364\0031\0031\0040-14\0030-14_27\003Pleszew\0033200365\0031\0031\0040-14\0030-14_28\003Pniewy\0033200575\0031\0031\0040-14\0030-14_29\003Pobiedziska\0033200576\0031\0031\0040-14\0030-14_30\003Poznań\0033200366\0031\0031\0040-14\0030-14_31\003Puszczykowo\0033200577\0031\0031\0040-14\0030-14_32\003Rawicz\0033200367\0031\0031\0040-14\0030-14_33\003Rogoźno\0033200578\0031\0031\0040-14\0030-14_34\003Słupca\0033200368\0031\0031\0040-14\0030-14_35\003Swarzędz\0033200369\0031\0031\0040-14\0030-14_36\003Szamotuły\0033200370\0031\0031\0040-14\0030-14_37\003Śrem\0033200371\0031\0031\0040-14\0030-14_38\003Środa Wielkopolska\0033200372\0031\0031\0040-14\0030-14_39\003Trzcianka\0033200373\0031\0031\0040-14\0030-14_40\003Trzemeszno\0033200579\0031\0031\0040-14\0030-14_41\003Turek\0033200374\0031\0031\0040-14\0030-14_42\003Wągrowiec\0033200375\0031\0031\0040-14\0030-14_43\003Witkowo\0033200580\0031\0031\0040-14\0030-14_44\003Wolsztyn\0033200376\0031\0031\0040-14\0030-14_45\003Wronki\0033200581\0031\0031\0040-14\0030-14_46\003Września\0033200377\0031\0031\0040-14\0030-14_47\003Złotów\0033200378\0031\0031\004\0030-15\003Zachodniopomorskie\0033200084\0031\0031\0040-15\0030-15_0\003Wszystkie Zachodniopomorskie\0033200084\0031\0030\0040-15\0030-15_1\003Barlinek\0033200379\0031\0031\0040-15\0030-15_2\003Białogard\0033200380\0031\0031\0040-15\0030-15_3\003Cedynia\0033200381\0031\0031\0040-15\0030-15_4\003Choszczno\0033200382\0031\0031\0040-15\0030-15_5\003Czaplinek\0033200586\0031\0031\0040-15\0030-15_6\003Darłowo\0033200383\0031\0031\0040-15\0030-15_7\003Dębno\0033200384\0031\0031\0040-15\0030-15_8\003Drawno\0033200385\0031\0031\0040-15\0030-15_9\003Drawsko Pomorskie\0033200386\0031\0031\0040-15\0030-15_10\003Goleniów\0033200387\0031\0031\0040-15\0030-15_11\003Gryfice\0033200388\0031\0031\0040-15\0030-15_12\003Gryfino\0033200389\0031\0031\0040-15\0030-15_13\003Kamień Pomorski\0033200390\0031\0031\0040-15\0030-15_14\003Kołobrzeg\0033200391\0031\0031\0040-15\0030-15_15\003Koszalin\0033200392\0031\0031\0040-15\0030-15_16\003Łobez\0033200393\0031\0031\0040-15\0030-15_17\003Międzyzdroje\0033200394\0031\0031\0040-15\0030-15_18\003Mielno\0033200395\0031\0031\0040-15\0030-15_19\003Myślibórz\0033200396\0031\0031\0040-15\0030-15_20\003Nowogard\0033200397\0031\0031\0040-15\0030-15_21\003Police\0033200398\0031\0031\0040-15\0030-15_22\003Połczyn-Zdrój\0033200582\0031\0031\0040-15\0030-15_23\003Pyrzyce\0033200399\0031\0031\0040-15\0030-15_24\003Sławno\0033200400\0031\0031\0040-15\0030-15_25\003Stargard Szczeciński\0033200401\0031\0031\0040-15\0030-15_26\003Szczecin\0033200402\0031\0031\0040-15\0030-15_27\003Szczecinek\0033200403\0031\0031\0040-15\0030-15_28\003Świdwin\0033200404\0031\0031\0040-15\0030-15_29\003Świnoujście\0033200405\0031\0031\0040-15\0030-15_30\003Trzebiatów\0033200583\0031\0031\0040-15\0030-15_31\003Wałcz\0033200406\0031\0031\0040-15\0030-15_32\003Wolin\0033200584\0031\0031\0040-15\0030-15_33\003Złocieniec\0033200585\0031\0031\004";var provinceSearchInputHtml='<input name="isProvinceSearch" type="hidden" value="true" />';$().ready(function(){function getURLParameter(name){return decodeURIComponent((location.href.match(RegExp("[QQ]"+name+'Z(.+?)(QQ|$)'))||[,null])[1]);}
var isProvinceSearch=getURLParameter('isProvinceSearch');document.frmSearchAd.Location.value=Math.abs(3200208);if(isProvinceSearch=='true'){var isProvinceSearchInput=$('input[name=isProvinceSearch]');if(isProvinceSearchInput.length>0){isProvinceSearchInput.val('true');}
else{$('#frmSearchAd').append(provinceSearchInputHtml);}}
$("#searchLoc").kjmenu_makeMenu({data:sdata,zindex:90000,cssWrapperClass:'nationalSite',OnSelect:function(mitem){var provinceSearchInput=$('input[name=isProvinceSearch]');if(mitem.value<-1){if(provinceSearchInput.length>0){provinceSearchInput.val('true');}
else{$('#frmSearchAd').append(provinceSearchInputHtml);}}
else{if(provinceSearchInput.length>0){provinceSearchInput.remove();}}
$("#searchLoc_name").html(mitem.name+"<img border='0' src='http://pic.classistatic.com/image/pics/classifieds/spacer.gif' width='25px' height='1px'/>");document.frmSearchAd.Location.value=Math.abs(mitem.value);$('.sfsp').remove();}});});addOnUnloadFunction('disableElement("searchAdGo")');var autoOptions={maxChars:4,hideLabel:'Ukryj',timeout:1,maxEntries:7,containerStyleClass:'keySpan',submitOnlick:true,baseUrl:"http://ac.classistatic.com/ac/10028/202/pl_PL/"};$(document).ready(function(){$("input.keyword").autocomplete1(autoOptions);$("#searchAdGo").click(function(){gAnalyticsPushForSearch("Click-Search",$(".newHeader input[name=distance]").val());});$("form#frmSearchAd").submit(function(){if($("#autoComp")[0].value==="Czego szukasz...?"){$("#autoComp")[0].value="";}
$("#searchAdGo").attr("disabled","true");return true;});});function gAnalyticsPushForSearch(srchType,numValue){}
var browsedata="\004\0030\003Nieruchomości\003http://www.gumtree.pl/fp-nieruchomosci/krakow/c2l3200208\004\0030\003Sprzedam\003http://www.gumtree.pl/fp-sprzedam/krakow/c4l3200208\004\0030\003Oferty Pracy\003http://www.gumtree.pl/fp-oferty-pracy/krakow/c8l3200208\004\0030\003Motoryzacja\003http://www.gumtree.pl/fp-motoryzacja/krakow/c5l3200208\004\0030\003Szukający Zatrudnienia\003http://www.gumtree.pl/fp-szukajacy-zatrudnienia/krakow/c9290l3200208\004\0030\003Moda\003http://www.gumtree.pl/fp-moda/krakow/c9541l3200208\004\0030\003Łodzie i Pojazdy wodne\003http://www.gumtree.pl/fp-lodzie-i-pojazdy-wodne/krakow/c9218l3200208\004\0030\003Elektronika\003http://www.gumtree.pl/fp-elektronika/krakow/c9237l3200208\004\0030\003Usługi\003http://www.gumtree.pl/fp-uslugi/krakow/c9l3200208\004\0030\003Dla Dziecka\003http://www.gumtree.pl/fp-dla-dziecka/krakow/c9459l3200208\004\0030\003Zwierzaki\003http://www.gumtree.pl/fp-zwierzaki/krakow/c9124l3200208\004\0030\003Sport i Rozrywka\003http://www.gumtree.pl/fp-sport-i-rozrywka/krakow/c9490l3200208\004\0030\003Społeczność\003http://www.gumtree.pl/fp-spolecznosc/krakow/c6l3200208\004\0030\003Oddam za darmo\003http://www.gumtree.pl/fp-krakow/l3200208?AdType=2&PriceAlternative=3\004\0030\003Wymiana/zamiana\003http://www.gumtree.pl/fp-krakow/l3200208?PriceAlternative=5";$(document).ready(function(){$("#AreaHomeTab,#SiteHomeTab").kjmenu_makeMenu({data:browsedata,OnSelect:function(mitem){document.location.replace(mitem.value);}});$("#changeLocDiv").click(function(){$.ajax({url:'http://www.gumtree.pl/c-GetLocation?CatId=0&PageName=',dataType:'script'});});});function trackHomeTabDropdown(type){var statisticUrl="";if(type=="tabname"){statisticUrl='http://www.gumtree.pl/c-Statistic?StatType=';}else if(type=="link"){statisticUrl='http://www.gumtree.pl/c-Statistic?StatType=HomeTabDropdownCount';}
statisticUrl=statisticUrl+'&ms='+new Date().getTime();$.get(statisticUrl);return true;}
var KNS=KNS||{};KNS.popWordSel='.floatLeft30px a';KNS.miscLabels=KNS.miscLabels||{};KNS.miscLabels.keyWordsLabelEn="Popular";$(document).ready(function(){$(KNS.popWordSel).click(function(){Kj.Ga.trackEventsinGA({category:'Clicks on '+KNS.miscLabels.keyWordsLabelEn+' Searches',action:'clicked word # '+($(KNS.popWordSel).index($(this))+1),opt_label:$(this).attr('href'),track_on_area_level:true});});});$(document).ready(function(){Kj.View.initViewAdActions({adId:'607878925',reportdata:"\0032\003Oszustwo/Zabronione\0032\004\0033\003Duplikat/Spam\0033\004\0035\003Nieaktualne\0035\004\0031\003W złej kategorii\0031\004\003r\003Wpisz powód...\003r",url:"http://www.gumtree.pl/c-illegalAdPanel"});});function doFlag(url){if(typeof(url)=='undefined'){return false;}
$("#pagestatus_new").css("display","");$.get('/c-ReportProblemByAjax?'+url,function(data){$("#pagestatus_new").html(data);});}
var currentModal;$(document).ready(function(){$('#doMisCat').click(function(e){var options={onOpen:function(){appendModalFrame();$("#modalframe").attr("src","http://www.gumtree.pl/c-wrongCategoryPanel");$('#modalFrameLayer').css('height',227);$('#modalframe').css('height',227);$('#modalFrameLayer').show();e.preventDefault();this.open(true);currentModal=this;}};$('#modalFrameLayer').modal(options);e.preventDefault();});});$(document).ready(function(){$('#doIllegalAd').click(function(e){var options={onOpen:function(){appendModalFrame();$("#modalframe").attr("src","http://www.gumtree.pl/c-illegalAdPanel");$('#modalFrameLayer').height(0);$('#modalFrameLayer').show();e.preventDefault();this.open(true);currentModal=this;}};$('#modalFrameLayer').modal(options);e.preventDefault();});});function scaleIllegalAdModal(height){$('#modalframe').css('height',height);$('#modalFrameLayer').css('height',height);$('#modalFrameLayer').css('margin-top',height/2*-1);}
function hideModal(){$('#modalframe').remove();currentModal.close(true);currentModal=null;}
function appendModalFrame(){$("#modalFrameLayer").append('<iframe name="modalframe" id="modalframe" width="100%" scrolling="no" frameborder="0" src="http://pic.classistatic.com/image/pics/classifieds/loading2.gif"></iframe>');}
function submitCategory(action,l1,l2){url="AdId=607878925&ViolationType=1";if(action=="submit"){try{url+="&L1CatId="+l1+"&L2CatId="+l2;}catch(err){}}
doFlag(url);hideModal();setTimeout('goTop()',800);}
function submitIllegal(action,email,msg){url="AdId=607878925&ViolationType=4";if(action=="submit"){try{url+="&Email="+email+"&Description="+msg;}catch(err){alert(err);}}
else{hideModal();return false;}
doFlag(url);hideModal();setTimeout('goTop()',800);}
function goTop(){$(document).scrollTop(0);}
var KNS=KNS||{};KNS.options=KNS.options||{};$(document).ready(function(){Kj.View.initThumbnailNavigator({pics:{fullImgUrl:'http://www.gumtree.pl/c-ViewAdLargeImage?AdId=607878925&Keyword=krakow',images:['http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/bvsAAOSwVFlT1949/$_35.JPG','http://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/gacAAOSwxCxT195J/$_35.JPG','http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/Tu0AAOSwPe1T195v/$_35.JPG','http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/EbQAAOSw7NNT1956/$_35.JPG','http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/lKUAAOSwRLZT196P/$_35.JPG','http://i.ebayimg.com/00/s/NzQ2WDEwMDA=/z/a78AAOSwEK9T196h/$_35.JPG','http://i.ebayimg.com/00/s/MTAwMFg3NDY=/z/bj4AAOSwEK9T1963/$_35.JPG','http://i.ebayimg.com/00/s/MTAwMFg3NTA=/z/JKUAAOSwQItT197E/$_35.JPG'],speed:400},totalCount:"8",videoCount:"0",catPath:"Properties/flat+%2F+house+for+rent"});});$(".view").load(function(){$(".imageStack").addClass("hideImageBackGrd");});$("img").load(function(){$(".imageStack2").addClass("hideImageBackGrd");});$(document).ready(function(){var init=false;$('.viewmap-link').click(function(){if(!init)
{init=true;Kj.Map.displayMap({canvas:"gmap",lat:"50.0067142",longitude:"19.889592100000073",addrTitle:'Adres',directionText:'Zobacz wskazówki dojazdu',adMarkers:[{addr:"Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska",pinType:"addr"}],hl:"pl",zoom:13},"http://maps.googleapis.com/maps/api/js?&client=gme-marktplaats&sensor=false&v=3.10");}});});$(function(){$(".viewmap-link").click(function(e){e.preventDefault();$.cachedScript("http://include.classistatic.com/include/e884/c3js/classifieds/rel1//common/jQuery/jquery.ui.dialog-min.js").done(function(script,textStatus){$("#viewmap-modal").dialog({width:800,modal:true,dialogClass:"dialog-view-image",title:"<span class='fLeft'>Doktora Józefa Babińskiego 23, 30-393 Kraków, Polska</span>",open:function(){$(".ui-icon-closethick").html(" ");},close:function(){$('meta[name="DCSext.page"]').attr("content","ViewAd");}});});});});var catpathvar={'sa606759499':'Properties/flat+%2F+house+for+rent','sa607359596':'Properties/flat+%2F+house+for+rent','sa607937278':'Properties/flat+%2F+house+for+rent','sa607315619':'Properties/flat+%2F+house+for+rent','sa607888553':'Properties/flat+%2F+house+for+rent'};$(document).ready(function(){$(".salink").click(function(e){Kj.Ga.trackEventsinGA({category:'SimilarAds',action:'SimilarAdClick',opt_label:catpathvar[$(e.target).parents('.salink').attr('id')],track_on_area_level:true});});});$(document).ready(function(){Kj.View.initMaskedPhone({catpath:'Properties/flat+%2F+house+for+rent',adId:"607 878 925",phoneRateLimiterEnabled:false,phoneLoggingEnabled:false,tryAgainLaterImg:"http://pic.classistatic.com/image/pics/classifieds/pl-PL/TryAgainLater.png",phoneImg:"http://ext.classistatic.com/imagesvc/txt2Img/GUEZdyU-ESoSSRTaZ2_migZN4p6ySNa6tvalAmTk8edZ_tEvl1pIsw0YiCmruWY7lfOS2C9fMOrYlqYYRLYuxlqlNZxEKQ3z3L3xROIA6g9VkYpUgu8BCpbDtF9G3dtl697ZG_0GJzgYQ8lfczz8grOcLGgqeZM5lmO6v_2TQ0kpivdwLq4RALJ0PcV45o6zjKe2rHWMA6IXrG9ukmK0xJeQ03Tyg_0iAwuL9yw9Rx8",hiddenPhoneImageUrl:"http://www.gumtree.pl/c-PhoneImage?ImageId=a89f3840607878925a53d9d43bz542720f259",phoneClickUrl:"http://www.gumtree.pl/c-UpdateClickCount?AdId=607878925&counterType=phone",isGAUpdated:false});});KNS.options.copyme="CopyMe";KNS.options.catpath='Properties/flat+%2F+house+for+rent';KNS.options.isGAUpdated=false;$(document).ready(function(){Kj.View.initReplyToAd(KNS.options);});$(document).ready(function(){Kj.View.initWebsiteClk({websiteClickUrl:'http://www.gumtree.pl/c-UpdateClickCount?AdId=607878925&counterType=website'});});$(document).ready(function(){$('#AreaHomeTab,#SiteHomeTab').click(function(e){trackHomeTabDropdown('tabname')});$('#AreaHomeText,#SiteHomeText').addClass('browse');var freeIcon=$('#freeIcon2');if(freeIcon.length>0){freeIcon.click(function(e){document.location='c-SelectCategory';return false;});}
$('.BigSearch').attachHoverPopup('#CategoryDropdown');});Kj.initReady({});
// End-TAIL JS
</script>
<!-- customJs -->
<!-- End of HtmlPageTail -->
<div id="flashCookie"></div>
<div id="myFavorites-panel"> </div>
<script>
Kj.initFavoritesFunctionality({domain:'www.gumtree.pl',panelActivated:'true',staticsPath:'http://include.classistatic.com/include/e884/c3js/classifieds/rel1/'});
</script>
</body></html>
"""
