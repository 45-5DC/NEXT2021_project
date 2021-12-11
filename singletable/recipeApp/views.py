from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# Create your views here.
def sendRecipePostList(request):
    try:
        recipe_posts = RecipePost.objects.all()
        json_recipes = []
        for recipe_post in recipe_posts:
            temp_recipe = {
                "title": recipe_post.title,
                "image": recipe_post.recipe_images[0],
		        "created_at": recipe_post.created_at,
		        "category": recipe_post.category,
            }
            json_recipes.append(temp_recipe)
        returnjson = json.dumps(json_recipes)
        return
    except Exception as ex:
        print(ex)


def sendCheckedRecipePostList(request):
    try:
        recipe_posts = RecipePost.objects.all()
        json_recipes = []
        for recipe_post in recipe_posts:
            temp_recipe = {
                "title": recipe_post.title,
                "image": recipe_post.recipe_images[0],
		        "author": recipe_post.author,
                "created_at": recipe_post.created_at,
		        "category": recipe_post.category,
                "comments_number": len(recipe_post.recipe_comments.all()),
                # "likes_number": recipe_post.like,
            }
            json_recipes.append(temp_recipe)
        returnjson = json.dumps(json_recipes)
        return
    except Exception as ex:
        print(ex)


# @login_required
def createRecipePost(request):
    if request.method == 'POST':
        new_recipe_post = RecipePost.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            author = request.user,
        )

        images = request.FILES.getlist('image')
        contents = request.POST.getlist('content')
        for i in range(len(images)):
            new_recipe_images = RecipeImages.objects.create(
                post = new_recipe_post,
                image = images[i],
                content = contents[i],
        )
        return
    return

# # 이미지-컨텐츠 연결 연습
# images = []
# raw_images = request.FILES.getlist('image')
# for i in range(len(raw_images)):
#     temp_image = {
#         'index': i,
#         'image': raw_images[i]
#     } # ~~ 프론트에서 이런식으로 보낸다고 하신건가?
#     images.append(temp_image)

# contents = []
# raw_contents = request.POST.getlist('content')
# for i in range(len(raw_contents)):
#     temp_content = {
#         'index': i,
#         'content': raw_contents[i]
#     }
#     contents.append(temp_content)

# for i in range(len(images)):
#     new_recipe_imagecontent = RecipeImages.objects.create(
#         post = new_recipe_post,
#         image = filter((lambda x: x['index'] == i), images)['image'],
#         content = filter((lambda x: x['index'] == i), contents)['content']
#     )
# # 모델의 형태를 아예 [{'index': 1, image: image1}, ...] 이런식으로 바꿔야하나?? 프론트로 다시 보낼 땐 어떡하지?


def sendRecipePostDetail(request, recipe_post_pk):
    try:
        recipe_post = RecipePost.objects.get(pk=recipe_post_pk)   
        json_recipe = {
            "title" : recipe_post.title,
            "created_at" : recipe_post.created_at,
            "updated_at" : recipe_post.updated_at,
            "category" : recipe_post.category,
            "author" : recipe_post.author,
            # "like" = recipe_post.like,
        }
        returnjson_recipe = json.dumps(json_recipe)
        return
    except Exception as ex:
        print(ex)


# 이미지와 컨텐츠를 json으로 묶어 프론트에 전달하기 위함
def sendRecipeImageContent(request, recipe_post_pk):
    try:
        recipe_post = RecipePost.objects.get(pk=recipe_post_pk)
        image_contents = recipe_post.recipe_images.all()
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


def sendRecipeCommentList(request, recipe_post_pk):
    try:
        recipe_post = RecipePost.objects.get(pk=recipe_post_pk)
        recipe_comments = recipe_post.recipe_comments.all()
        json_recipe_comments = []
        for comment in recipe_comments:
            temp_comment = {
                "comment_author": comment.author,
                "comment_content": comment.content,
            }
            json_recipe_comments.append(temp_comment)
        returnjson_comments = json.dumps(json_recipe_comments)
        return
    except Exception as ex:
        print(ex)

# @login_required
def createRecipeComment(request, recipe_post_pk):
    recipe_post = RecipePost.objects.get(pk=recipe_post_pk)

    if request.method == 'POST':
        new_comment = RecipeComment.objects.create(
            post = recipe_post,
            content = request.POST['content'],
            author = request.user,
        )
        return
    return

# {% if user.is_authenticated %} / {% if user.is_authenticated and comment.author.pk == user.pk %}
# 기존에 html에서 처리하던 이런 부분은 프론트에서??

def deleteRecipePost(request, recipe_post_pk):
    recipe_post = RecipePost.objects.get(pk=recipe_post_pk)
    recipe_post.delete()
    return

def deleteRecipeComment(request, recipe_post_pk, recipe_comment_pk):
    recipe_comment = RecipeComment.objects.get(pk=recipe_comment_pk)
    recipe_comment.delete()
    return

def updateRecipePost(request, recipe_post_pk):
    recipe_post = RecipePost.objects.get(pk=recipe_post_pk)

    if request.method == 'POST':
        RecipePost.objects.filter(pk=recipe_post_pk).update(
            title = request.POST['title'],
            category = request.POST['category'],
            author = request.user,
            # like = ,
        )

        new_images = request.FILES.getlist('image')
        new_contents = request.POST.getlist('content')
        recipe_imagecontent = recipe_post.recipe_images.all()
        # recipe_imagecontent = RecipeImages.objects.filter(post.pk=recipe_post_pk)
        
        for i in range(len(new_images)):
        # 기존 게시물보다 사진-내용 늘 경우...
            if i > len(recipe_imagecontent)-1:
                RecipePost.objects.create(
                    post = recipe_post,
                    image = new_images[i],
                    content = new_contents[i],
                )

        # 메인 수정 부분
            else:
                recipe_imagecontent[i].post = recipe_post
                recipe_imagecontent[i].image = new_images[i]
                recipe_imagecontent[i].content = new_contents[i]
                recipe_imagecontent[i].save()

        # 기존 게시물보다 사진-내용 줄 경우...
        if len(new_images) < len(recipe_imagecontent):
            recipe_imagecontent[len(new_images)-1:].delete()
        return
    return

# 기존 html에서 <input value="{{post.title}}" /> 이런 식으로 불러오던 기존 포스트의 정보는 프론트에서?

# 이미지 업데이트 기존
        # images = request.FILES.getlist('image')
        # contents = request.POST.getlist('content')
        # for i in range(len(images)):
        #     recipe_post.recipe_images.all().update(
        #     # RecipeImages.objects.filter(post.pk=recipe_post_pk).update(
        #         post = recipe_post,
        #         image = images[i],
        #         content = contents[i],
        #     )