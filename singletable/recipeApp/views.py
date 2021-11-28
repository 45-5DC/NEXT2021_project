from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def page9_send_recipeposts_list(request):
    try:
        recipe_posts = RecipePost.objects.all()
        json_recipes = []
        for recipe_post in recipe_posts:
            temp_recipe = {
                "title": recipe_post.title,
                "image": recipe_post.recipe_images[0], # 2안) 이건 될듯?
		        "created_at": recipe_post.created_at,
		        "category": recipe_post.category, # 카테고리 불러와서 이에 해당하는 게시글 보여주려면 이것도 1대다여야 하지않을까? ~ 이건 프론트에서 직접 작성하여 불러오는 방향으로
            }
            json_recipes.append(temp_recipe)
        returnjson = json.dumps(json_recipes)
        return
    except Exception as ex:
        print(ex)

# # 기존
#     try:
#         recipe_posts = RecipePost.objects.all()
#         json_recipes = []
#         for recipe_post in recipe_posts:
#             temp_recipe = {
#                 "title": recipe_post.title,
# 		        "image": recipe_post.recipe_images.objects.get(pk=1), # (에러 가능) 여러 개 중에 하나만 어떻게 가져와야 할까. 모델에서 썸네일을 따로 빼는 것도 좋을 듯듯?
# 		        "created_at": recipe_post.created_at,
# 		        "category": recipe_post.category, # 카테고리 불러와서 이에 해당하는 게시글 보여주려면 이것도 1대다여야 하지않을까? ~ 이건 프론트에서 직접 작성하여 불러오는 방향으로
#             }
#             json_recipes.append(temp_recipe)
#         returnjson = json.dumps(json_recipes)
#         return
#     except Exception as ex:
#         print(ex)


def page10_11_send_checked_recipeposts_list(request):
    try:
        recipe_posts = RecipePost.objects.all()
        json_recipes = []
        for recipe_post in recipe_posts:
            temp_recipe = {
                "title": recipe_post.title,
                "image": recipe_post.recipe_images[0], # 2안) 이건 될듯?
		        "author": recipe_post.author.nickname,
                "created_at": recipe_post.created_at,
		        "category": recipe_post.category,
                "comments_number": len(recipe_post.recipe_comments.objects.all()),
                # "likes_number": recipe_post.like,
            }
            json_recipes.append(temp_recipe)
        returnjson = json.dumps(json_recipes)
        return
    except Exception as ex:
        print(ex)

# 기존
    # try:
    #     recipe_posts = RecipePost.objects.all()
    #     json_recipes = []
    #     for recipe_post in recipe_posts:
    #         temp_recipe = {
    #             "title": recipe_post.title,
	# 	        "image": recipe_post.recipe_images.objects.get(pk=1), # (에러 가능) 여러 개 중에 하나만 어떻게 가져와야 할까. 모델에서 썸네일을 따로 빼는 것도 좋을 듯
	# 	        "author": recipe_post.author.nickname,
    #             "created_at": recipe_post.created_at,
	# 	        "category": recipe_post.category,
    #             "comments_number": len(recipe_post.recipe_comments.objects.all()),
    #             # "likes_number": recipe_post.like,
    #         }
    #         json_recipes.append(temp_recipe)
    #     returnjson = json.dumps(json_recipes)
    #     return
    # except Exception as ex:
    #     print(ex)


def page12(request):
    # 카테고리 정보를 보내야할 것 같다. 그러려면 1대다여야 하지않을까? --> 프론트에서 직접 작성하여 불러오는 방향으로.
    return


@login_required
def page14_15_create_recipepost(request):
    if request.method == 'POST':
        new_recipe_post = RecipePost.objects.create(
            title = request.POST['title'],
            # created_at = 
            # updated_at = 
            category = request.POST['category'],
            author = request.user, # request.user.profile.nickname
            # like = ,
        )

        images = request.FILES.getlist('image')
        contents = request.POST.getlist('content')
        for i in range(len(images)):
            new_recipe_images = RecipeImages.objects.create(
                post = new_recipe_post,
                image = images[i],
                content = contents[i],
        )
        # for (recipe_image, image_content) in zip(request.FILES.getlist('image'), request.POST.getlist('content')):
        #     new_recipe_images = RecipeImages.objects.create(
        #         post = new_recipe_post,
        #         image = recipe_image,
        #         content = image_content,
        #     ) 
        return
    return

# # 기존
#     if request.method == 'POST':
#         new_recipe_post = RecipePost.objects.create(
#             title = request.POST['title'],
#             content = request.POST['content'],
#             # created_at = 
#             # updated_at = 
#             category = request.POST['category'],
#             author = request.user, # request.user.profile.nickname
#             # like = ,
#         )
#         for recipe_image in request.FILES.getlist('image'):
#             new_recipe_images = RecipeImages.objects.create(
#                 post = new_recipe_post,
#                 image = recipe_image,
#             )
#             return
#     return




def page16_17_send_recipepost_detail(request, recipe_post_pk):
    try:
        recipe_post = RecipePost.objects.get(pk=recipe_post_pk)   
        json_recipe = {
            "title" : recipe_post.title,
            # "content" : recipe_post.content, # image 보내는 함수에서 같이 보내기
            "created_at" : recipe_post.created_at,
            "updated_at" : recipe_post.updated_at,
            "category" : recipe_post.category,
            "author" : recipe_post.author.nickname, # user만? profile만?
            # "like" = recipe_post.like,
        }
        returnjson_recipe = json.dumps(json_recipe)
        return
    except Exception as ex:
        print(ex)


# 이미지와 컨텐츠를 json으로 묶어 프론트에 전달하기 위함
def page16_17_send_recipeimagecontent(request, recipe_post_pk):
    try:
        recipe_post = RecipePost.objects.get(pk=recipe_post_pk)
        image_contents = recipe_post.recipe_images.all() # 2안) objects. 제거
        json_image_contents = []
        for i in range(len(image_contents)):
            temp_image_content = {
                "image" + str(i+1) : image_content.image.url[i],
                "content" + str(i+1) : image_content.content[i]
            }
            json_image_contents.append(temp_image_content)
        returnjson_image_contents = json.dumps(json_image_contents)
        return
    except Exception as ex:
        print(ex)


def page16_17_send_recipecomments_list(request, recipe_post_pk):
    try:
        recipe_post = RecipePost.objects.get(pk=recipe_post_pk)
        recipe_comments = recipe_post.recipe_comments.all()
        json_recipe_comments = []
        for comment in recipe_comments:
            temp_comment = {
                "comment_author": comment.profile.nickname,
                "comment_content": comment.content,
            }
            json_recipe_comments.append(temp_comment)
        returnjson_comments = json.dumps(json_recipe_comments)
        return
    except Exception as ex:
        print(ex)

@login_required
def page16_17_create_recipecomment(request, recipe_post_pk):
    recipe_post = RecipePost.objects.get(pk=recipe_post_pk)

    if request.method == 'POST':
        new_comment = RecipeComment.objects.create(
            post = recipe_post,
            content = request.POST['content'],
            author = request.user, # request.user.profile.nickname
        )
        return
    return

# {% if user.is_authenticated %} / {% if user.is_authenticated and comment.author.pk == user.pk %}
# 기존에 html에서 처리하던 이런 부분은 프론트에서??

def delete_recipepost(request, recipe_post_pk):
    recipe_post = RecipePost.objects.get(pk=recipe_post_pk)
    recipe_post.delete()
    return

def delete_recipecomment(request, recipe_post_pk, recipe_comment_pk):
    recipe_comment = RecipeComment.objects.get(pk=recipe_comment_pk)
    recipe_comment.delete()
    return

def update_recipepost(request, recipe_post_pk):
    recipe_post = RecipePost.objects.get(pk=recipe_post_pk)

    if request.method == 'POST':
        RecipePost.objects.filter(pk=recipe_post_pk).update(
            title = request.POST['title'],
            # content = request.POST['content'],
            # created_at = 
            # updated_at = 
            category = request.POST['category'],
            author = request.user, # request.user.profile.nickname
            # like = ,
        )

        images = request.FILES.getlist('image')
        contents = request.POST.getlist('content')
        for i in range(len(images)):
            recipe_post.recipe_images.all().update(
            # RecipeImages.objects.filter(post.pk=recipe_post_pk).update(
                post = recipe_post,
                image = images[i],
                content = contents[i],
            )
        return
    return

# 기존 html에서 <input value="{{post.title}}" /> 이런 식으로 불러오던 기존 포스트의 정보는 프론트에서?