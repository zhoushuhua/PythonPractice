from string import Template

# 返回响应文件类型默认为html文件
def start_response(resp = "text/html"):
    return("Content-Type:" + resp + "\n\n")

# 加载html头部
def include_header(the_title):
    file_name="templates/header.html"
    try:
        with open(file_name) as headf:
            head_text = headf.read()
        header = Template(head_text)
        return(header.substitute(title = the_title))
    except IOError as error:
        print("Read " + file_name + " error:" + str(error))
    return(None)

# 加载html尾部 参数为字典集合
def include_footer(the_links={}):
    file_name="templates/footer.html"
    try:
        # 读取文件
        with open(file_name) as footf:
            foot_text = footf.read()
        
        link_string = ""
        for key in the_links:
            link_string += "<a href=\"" + the_links[key] + "\">"+key+"</a>&nbsp;&nbsp;&nbsp;&nbsp;"
        footer = Template(foot_text)
        return(footer.substitute(links=link_string))
    except IOError as error:
        print("Read " + file_name + " error:" + str(error))
    return(None)

# 加载开始表单
def start_form(the_url, form_type="GET"):
    return("<form action=\"" + the_url + "\" method=\"" + form_type + "\">")

# 加载结束表单
def end_form(submit_msg="submit"):
    return("<p></p><input type=\"submit\" value=\"" + submit_msg + "\" /></form>")

# 加载单选按钮
def radio_button(rb_name, rb_value):
    return("<input type=\"radio\" name=\"" + rb_name + "\" value=\"" + rb_value + "\" />" + rb_value + "<br />")

# 加载列表
def u_list(items):
        u_string='<ul>'
        for item in items:
            u_string += '<li>' + item + '</li>'
        u_string += '</ul>'
        return(u_string)

# 加载标题
def header(header_text, header_level=2):
    return('<h'+str(header_level)+'>'+header_text+'</h'+str(header_level)+'>')

# 加载段落
def para(para_text):
    return('<p>'+para_text+'</p>')

# 创建输入表单项
def create_inputs(inputs_list):
    html_inputs = ""
    for input_name in inputs_list:
        html_inputs += '<input type="text" name="'+input_name+'" />&nbsp;&nbsp;<br/>'
    return(html_inputs)

# 创建表单
def do_from(name, the_inputs, method="POST", text="Submit"):
    # 定义模板文件名
    file_name = "templates/form.html"
    try:
        # 读取文件
        with open(file_name) as formf:
            form_text = formf.read()
        form = Template(form_text)
        # 创建输入框
        inputs = create_inputs(the_inputs)

        # 创建表单
        return(form.substitue(cgi_name=name, http_method=method, list_of_inputs=inputs, submit_text=text))
    except IOError as error:
        print("Read " + file_name + " error:" + str(error))
    return(None)
