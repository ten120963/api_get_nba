from django.shortcuts import render, redirect

def home(request):
	
	import requests
	import json

	if request.method == "POST":
		team = request.POST['team']
		api_request = requests.get("https://www.balldontlie.io/api/v1/games?seasons[]=2018&team_ids[]=" + str(team))

		try:
			api = json.loads(api_request.content)
			test_list = (api["data"])
			
			'''	
			new_dict = (test_list[0])
			home_team = new_dict["home_team"]
			visitor_team = new_dict["visitor_team"]
			home_team_score = new_dict["home_team_score"]
			visitor_team_score = new_dict["visitor_team_score"]
			home_dict = new_dict["home_team"]
			visitor_dict = new_dict["visitor_team"]
			home_full_name = home_dict['full_name']
			visitor_full_name = visitor_dict['full_name']	
			'''	
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {
		'api': api,
		'test_list': test_list		
		})
			
	else:
		return render(request, 'home.html', {'team': "Enter a team ID above"})
	

def about(request):
	return render(request, 'about.html', {})	