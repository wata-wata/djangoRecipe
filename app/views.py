from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.views.generic import View
from django.views.generic.base import TemplateView

REQUEST_URL = "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426"
APP_ID = "1008575362204726338"

class IndexView(TemplateView):
	template_name = 'home/index.html'
	
class ResultView(View):
	
	def get(self, request, *args, **kwargs):
		categories = self.request.GET.getlist('categories[]',[])
		if categories != []:
			recipes = []
			recipe_id = []
			recipe_num_dict = []
			result = []
			i = 0
			for category in categories:
				search_param = {
					"applicationId":[APP_ID],
					#"formatVersion":2,
					"categoryId":category
				}
				responses = requests.get(REQUEST_URL, search_param).json()
				if 'error' in responses:
					break
				recipes.append(responses["result"])
				j = 0
				for recipe in responses["result"]:
					recipe_num = {
						"cat_rank":i,
						"res_rank":j
					}
					if recipe["recipeId"] in recipe_id:
						head_id = recipe["recipeId"]
						recipe_num_dict.pop(recipe_id.index(head_id))
						recipe_id.pop(recipe_id.index(head_id))
						recipe_num_dict.insert(0,recipe_num)
						recipe_id.insert(0,head_id)
					else:
						recipe_num_dict.append(recipe_num)
						recipe_id.append(recipe["recipeId"])
					j += 1
				i += 1
			for recipes_num in recipe_num_dict:
				result.append(recipes[recipes_num["cat_rank"]][recipes_num["res_rank"]])
			return render(request,'home/searchResult.html',{ "result":result })
		else:
			return redirect('djangoRecipe:index')
			
class SiteUserLoginView(View):
    def get(self, request, *args, **kwargs):

        return render(request, "app/siteUser/login.html")
		
	
	
