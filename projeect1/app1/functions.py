def handle_uploaded_file(f):
    with open('app1/static/upload/'+f.name,'wb+') as destinantion:
        for chunk in  f.chunks():
            destinantion.write(chunk)
