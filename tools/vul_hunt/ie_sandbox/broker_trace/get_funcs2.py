from broker_calls import *

l1 = get_shdocvw_calls_name()
l2 = get_ierecovery_store_calls_name()
l3 = get_settingsstore_calls_name()
l4 = get_ieuser_calls_name()
l5 = get_stdidentity_unk_calls_name()
l6 = get_ieaxinstall_calls_name()
l7 = get_iereghelperbroker_calls_name()
l8 = get_iereghelperobject_cleanup_calls_name()
l9 = get_iebrokerattach_calls_name()
l0 = get_protectedmodeAPI_calls_name()
l11 = get_shellwindow_calls_name()

iface_dict = {
    '''"shdocvw" : l1,
    "recoverystore" : l2,
    "settingsstore" : l3,
    "ieuser" : l4,
    "stdidentity" : l5,
    "ieaxinstall" : l6,
    "iereghelperbroker" : l7,
    "iereghelperobject" : l8,
    "iebrokerattach" : l9,
    "protectedmodeAPI" : l0,'''
    "shellwindow": l11
}


def gen_funcs():

    for i in iface_dict.keys():
        print "\n\nFUNCTIONS FOR %s \n\n" %i

        for f in iface_dict[i]:

            args = f.split(":")[-1].split("(")[1][:-1]
            func = f.split(":")[-1].split("(")[0]
            #func = f.split("(")[0]
    
            if "ushort" in args:
                args = args.replace("ushort", "unsigned short")

            if "ulong" in args:
                args = args.replace("ulong", "unsigned long")
    
            if "uchar" in args:
                args = args.replace("uchar", "unsigned char")

            if "uint" in args:
                args = args.replace("uint", "unsigned int")

            #args = args.split(",")

            print "void (*" + func + ")(HANDLE, " + args + ");"
            '''s = "(\"" + func + "\"," + "[\""
            for i in args:
                s = s + i + "\",\""

            print s[:-2] + "]"'''




gen_funcs()
