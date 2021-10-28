from django.shortcuts import render

# Create your views here.
from RE_property.models import Property
from RE_user.models import SiteUser


def get_agent_list(request):
    agents = SiteUser.objects.all()
    ag_li = [ag for ag in agents]
    grouped_agents = agent_grouper(ag_li)
    context = {'agents': grouped_agents}
    return render(request, 'agent_list.html', context)



def get_agent_profile(request,*args,**kwargs):
    agent_id = kwargs['agent_id']
    agent = SiteUser.objects.get(id=agent_id)
    objects = Property.objects.filter(user=agent)


    context = {
        'agent' : agent,
        'property' : objects
    }

    return render(request, 'agent_profile.html',context)

def agent_grouper(images: list) -> dict:
    li = []
    dic = {}
    counter = 0
    for img in images:
        li.append(img)
        if len(li) == 6:
            dic[counter] = li
            li = []
            counter += 1
    dic[counter] = li
    return dic
