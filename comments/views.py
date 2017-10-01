from django.shortcuts import render
from django.http import HttpResponse

from comments.models import  Comments

# Create your views here.

def instance_comments(requests,object_id):
	comments = Comments.objects.all().filter(object_id=object_id).distinct()
	st = '<div class="bootstrap snippet">\
    <div class="row">\
		<div class="col-md-12">\
		    <div class="blog-comment">\
                <hr/>\
				<ul class="comments">'+createComment(comments)+'</ul>\
			</div>\
		</div>\
	</div>\
</div>'
	return HttpResponse(st)

def createComment(comments):
	st = ""
	for i in comments:
		st+='<li class="clearfix">\
				  <img src="https://bootdey.com/img/Content/user_2.jpg" class="avatar" alt="">\
				  <div class="post-comments">\
				      <p class="meta">'+str(i.timestamp)+' \
				      <a href="#">'+str(i.user)+'\
				      </a> says : <i class="pull-right"><a href="#"><small>Reply</small></a></i></p>\
				      <p>\
				      	'+str(i.content)+'\
				      </p>\
				  </div>\
				  <ul class="comments">\
				      '+createComment(i.childer())+'\
				  </ul>\
				</li>'
				# +str(i.id)+" "+i.content+"<ul>"+createComment(i.childer())+"</ul>"+"</li>"
	return st



"""

<div class="container bootstrap snippet">\
    <div class="row">\
		<div class="col-md-12">\
		    <div class="blog-comment">\
				<h3 class="text-success">Comments</h3>\\
                <hr/>\
				<ul class="comments">\
				<li class="clearfix">
				  <img src="https://bootdey.com/img/Content/user_1.jpg" class="avatar" alt="">
				  <div class="post-comments">
				      <p class="meta">Dec 18, 2014 <a href="#">JohnDoe</a> says : <i class="pull-right"><a href="#"><small>Reply</small></a></i></p>
				      <p>
				          Lorem ipsum dolor sit amet, consectetur adipiscing elit.
				          Etiam a sapien odio, sit amet
				      </p>
				  </div>
				</li>
				<li class="clearfix">\
				  <img src="https://bootdey.com/img/Content/user_2.jpg" class="avatar" alt="">\
				  <div class="post-comments">\
				      <p class="meta">Dec 19, 2014 <a href="#">JohnDoe</a> says : <i class="pull-right"><a href="#"><small>Reply</small></a></i></p>\
				      <p>\
				          Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
				          Etiam a sapien odio, sit amet\
				      </p>\
				  </div>\
				  <ul class="comments">\
				      <li class="clearfix">\
				          <img src="https://bootdey.com/img/Content/user_3.jpg" class="avatar" alt="">\
				          <div class="post-comments">\
				              <p class="meta">Dec 20, 2014 <a href="#">JohnDoe</a> says : <i class="pull-right"><a href="#"><small>Reply</small></a></i></p>\
				              <p>\
				                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
				                  Etiam a sapien odio, sit amet\
				              </p>\
				          </div>\
				      </li>\
				  </ul>\
				</li>
				</ul>\
			</div>\
		</div>\
	</div>\
</div>\
"""