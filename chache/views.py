from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json,random,datetime

@login_required
def index(request):
	#return HttpResponse(u"大家好啊！！！")
	#List = map(str, range(7))
	#string = "lumit"
	#index_name = {"index":"pad1", "index2":"pad2", "index3":"pad3"}
	#context1 = {'string': "John Doe",'index_name':index_name, "list":List}
	#return render(request, 'chache/index.html', context1)
	data1_list = []
	data2_list = []
	#value1_list = []
	for i in range(7):	
		data1_list.append([2002,1,i+1,random.randrange(10)*i+120])
		data2_list.append([2002,1,i+1,random.randrange(20)*i+120])
	
	value1_list = {"hello":1,"a":2,"b":3}
	#叉车总数
	chache_count = 2500
	#叉车增长率
	chache_increase = 0.04;

	chart_plot_01_settings = {"series": {
        "lines": {
          "show": False,
          "fill": True
        },
        "splines": {
          "show": True,
          "tension": 0.4,
          "lineWidth": 1,
          "fill": 0.4
        },
        "points": {
          "radius": 0,
          "show": True
        },
        "shadowSize": 2
      },
      "grid": {
        "verticalLines": True,
        "hoverable": True,
        "clickable": True,
        "tickColor": "#d5d5d5",
        "borderWidth": 1,
        "color": '#fff'
      },
      "colors": ["rgba(38, 185, 154, 0.38)", "rgba(3, 88, 106, 0.38)"],
      "xaxis": {
        "tickColor": "rgba(51, 51, 51, 0.06)",
        "mode": "time",
        "tickSize": [1, "day"],
        #"tickLength": 10,
        "axisLabel": "Date",
        "axisLabelUseCanvas": True,
        "axisLabelFontSizePixels": 12,
        "axisLabelFontFamily": 'Verdana, Arial',
        "axisLabelPadding": 10
      },
      "yaxis": {
        "ticks": 8,
        "tickColor": "rgba(51, 51, 51, 0.06)",
      },
      "tooltip": False
    }
	
	context1 = {"data1_list":json.dumps(data1_list),"data2_list":json.dumps(data2_list),"value1_list":json.dumps(value1_list),
				"chache_count":json.dumps(chache_count),"chache_increase":chache_increase*100,"chart_plot_01_settings":json.dumps(chart_plot_01_settings),}
	return render(request, 'index.html', context1)
	#lumit = u"lumit"
	#return render(request, 'app/index.html' , {user_name: lumit})
@login_required
def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

@login_required
def add2(request, a , b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

@login_required
def appviews(request, viewname):
	index_name = {"index":"pad1", "index2":"pad2", "index3":"pad3"}
	context1 = {'string': "John Doe",'index_name':index_name}
	return render(request, viewname+'.html', context1)

@login_required
def ajax_list(request):
  data1_list = []
  
  #value1_list = [] [116.397428+Math.random()*i, 39.90923+Math.random()*i]
  for i in range(34):  
    #data1_list.append([116397428+random.randrange(10)*1000*i,random.randrange(10)*1000*i+39909230])
    #经度，纬度，运行时间(单位秒），工作时间，电量，报警号
    date1 = datetime.timedelta(seconds=random.randrange(1000000))
    date2 = datetime.timedelta(seconds=random.randrange(1000000))
    data1_list.append(['{0:.6f}'.format(116.397428+random.randrange(10)*0.001*i),'{0:.6f}'.format(random.randrange(10)*0.001*i+39.909230),
      '{0}天{1}小时{2}分'.format(date1.days,date1.seconds//3600,(date1.seconds%3600)//60),'{0}天{1}小时{2}分'.format(date2.days,date2.seconds//3600,(date2.seconds%3600)//60),
      '{0}%'.format(random.randrange(100)),'报警号N008{0}'.format(random.randrange(1000))])
  return JsonResponse(data1_list,safe=False)

@login_required
def ajax_dict(request):
  name_dict = {'twz':'Love pyphon and Django', 'zqxt':'I am learning Django'}
  return JsonResponse(name_dict)

#def favicon(request):
#	return HttpResponse(request,'')