import yate
import cgitb

# 打开调试
cgitb.enable()

# 输出
print(yate.start_response())
print(yate.do_form("/cgi-bin/add_timing_data.py", ['TimeValue'], text = 'Send'))
