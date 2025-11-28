def get_type_id_from_link(link):
    segments = link.split('/')
    type = segments[-2]
    id = segments[-1].split('?')[0]
    return (type, id)