from django.shortcuts import render
from datetime import date
from nsepy import get_history

# Create your views here.

def index(request):
    return render(request,'index.html')

def header(request):
    return render(request,'header.html')

def stock_view(request):
    context = {}
    context['page_title'] = 'View Stock'
    return render(request,'search-stock.html',context=context)

def stock_search(request):

    try:
        symbol = request.GET.get('symbol')
        start = request.GET.get('start').split('-')
        end = request.GET.get('end').split('-')
    except:
        start = date(2022,5,1)
        end = date().today()
        symbol = 'SBIN'
    sbin = get_history(symbol=symbol,
                    start=date(int(start[0]),int(start[1]),int(start[2])),
                    end=date(int(end[0]),int(end[1]),int(end[2])))
    d = dict(sbin)
    
    data = {'Info': {'Symbol' : 'SBIN'}, 'Time' : {}}
    for i in range(7):
        try:
            data['Info']['Series'] = d['Series'][date(2022,3,i)]
        except:pass
    l = ['Open','High','Low','Close']
    for k,v in d['Symbol'].items():
        data['Time'].update({str(k):{'date':str(k)}})
    for i in l:
        for k,v in d[i].items():
            data['Time'][str(k)].update({i.lower():v})

    context = {}
    context['page_title'] = 'History Of stock'
    context['data'] = data
    context['open_max'] = sbin['Open'].max()
    context['open_min'] = sbin['Open'].min()
    context['open_avg'] = round(sbin['Open'].mean(),2)
    context['close_max'] = sbin['Close'].max()
    context['close_min'] = sbin['Close'].min()
    context['close_avg'] = round(sbin['Close'].mean(),2)

    context['high_max'] = sbin['High'].max()
    context['high_min'] = sbin['High'].min()
    context['high_avg'] = round(sbin['High'].mean(),2)

    context['low_max'] = sbin['Low'].max()
    context['low_min'] = sbin['Low'].min()
    context['low_avg'] = round(sbin['Low'].mean(),2)


    return render(request,'search-stock.html',context=context)