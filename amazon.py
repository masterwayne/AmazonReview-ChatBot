import requests
import urllib
import json
given_url = 'http://www.amazon.in/gp/product/B01GRFC3E2/ref=s9_acsd_ri_bw_c_x_2_r?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-7&pf_rd_r=0HA8W81FD300923GQM41&pf_rd_r=0HA8W81FD300923GQM41&pf_rd_t=101&pf_rd_p=00600dcf-3c0f-4d68-b3a4-c57df8f5892f&pf_rd_p=00600dcf-3c0f-4d68-b3a4-c57df8f5892f&pf_rd_i=1375424031'
send_url = urllib.quote_plus(given_url)
ini='http://api.diffbot.com/v3/discussion?token=818203f4d98d7a6a10519a2869c759dd&url='+send_url
res=requests.get(ini)
data = json.loads(res.text)
size = len(data['objects'][0]['posts'])
for i in range(0,size):
	print "reviewer name:  "+data['objects'][0]['posts'][i]['author']
	print "revew:   "+data['objects'][0]['posts'][i]['text'].encode('ascii','ignore')
	print "                                                                     "
