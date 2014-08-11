# -*- coding: UTF-8 -*-

import re

def extractOffer(html):
        title = extractTitle(html)
        date = extractDate(html)
        price = extractPrice(html)
        addressSection = extractAddress(html)
        description = extractDescription(html)
        summary = extractSummary(html)
        imageUrl = extractImageUrl(html)
        
        offer = {"title" : title,
                 "date" : date,
                 "price" : price,
                 "addressSection" : addressSection,
                 "description" : description,
                 "summary" : summary,
                 "imageUrl" : imageUrl}
        return offer    

def extractPrice(offerHtml):
    START_TAG = "<td style='font-weight:bold'>"
    STOP_TAG = "</td>"
    return getStringBetween(offerHtml, START_TAG, STOP_TAG)

def extractDate(offerHtml):
    START_TAG = '<td class="first_row" >'
    STOP_TAG = '</td>'
    return getStringBetween(offerHtml, START_TAG, STOP_TAG)

def extractTitle(offerHtml):
    START_TAG = '<title>'
    STOP_TAG = '</title>'
    return getStringBetween(offerHtml, START_TAG, STOP_TAG)

def extractAddress(offerHtml):
    START_TAG = u'<td itemscope itemtype="http://schema.org/Place">'
    STOP_TAG = u'</td>'
    address = getStringBetween(offerHtml, START_TAG, STOP_TAG)
    address = address.replace(u"Pokaż mapę", "")
    return stripTextFromHtmlTags(address).strip()

def extractDescription(offerHtml):
    START_TAG = '<span id="preview-local-desc">'
    STOP_TAG = '</span>'
    desciption = getStringBetween(offerHtml, START_TAG, STOP_TAG)
    return stripTextFromHtmlTags(desciption)

def extractSummary(offerHtml):
    START_TAG = 'property="og:description" content="'
    STOP_TAG = '"/>'
    summary = getStringBetween(offerHtml, START_TAG, STOP_TAG)
    return stripTextFromHtmlTags(summary)

def extractImageUrl(offerHtml):
    START_TAG = '<meta property="og:image" content="'
    STOP_TAG = '"/>'
    return getStringBetween(offerHtml, START_TAG, STOP_TAG)   

def stripTextFromHtmlTags(text):
    return re.sub('<[^<]+>', '', text)

def getStringBetween(source, start, stop):
    iStart = source.find(start) + len(start)
    iStop = source.find(stop, iStart)
    return source[iStart:iStop].strip()