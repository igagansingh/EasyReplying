import json
import requests

#Edit here, whatever message you want to set to
AUTOMATED_REPLY="Wow!"

#Follow 'https://developers.facebook.com/tools/explorer' and generate your access_token
access_token='access_token=<YOUR TOKEN ID>'

#URL that would return who the post is by, post_id (essential for replying to that particular post) and the contents of
#it in JSON fromat. You can do a lot of other things, explore here : 'https://developers.facebook.com/tools/explorer'
request_url='https://graph.facebook.com/v2.8/me/?fields=feed%7Bmessage%2Cfrom%7D&'+access_token

#Actual request for the above url
r = requests.get(request_url)

#Getting the data back after successful request 
data = json.loads(r.text)

#Calculating the number of posts on the given page
length_of_posts = len(data['feed']['data'])

#Iterate over each of the post
for i in range(0,length_of_posts):
	#Getting the name of the person who posted
	by = data['feed']['data'][i]['from']['name']
	#The unique id pointing to the post to which this script will reply
	post_id = data['feed']['data'][i]['id']
	#Sometimes the message section(i.e. The post content) may have nothing(usually when you've shared some link or video)
	# in it so a try block to handle that cases. 
	try:
		message = data['feed']['data'][i]['message']
	except:
		message = 'NO MESSAGE'
	
	#A sample of the 3 things extracted
	print(by+ '\t'+ message+ '\t'+ post_id)
	
	#URL for reply to the post selected
	reply_url='https://graph.facebook.com/'+post_id+'/comments/?'+access_token+'&message='+AUTOMATED_REPLY
	#The actual post request to perform the reply task
	requests.post(reply_url)
	print()

#In case birthday wishes increase than 25 (or set limit while at : 'https://developers.facebook.com/tools/explorer' )
#this time when requesting data remove the ['feed'] (Try it out while exploring)
next_page_url=data['feed']['paging']['next']

#A lot of updates coming
print("DONE!")