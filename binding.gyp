{
    "targets": [{
            "target_name": "native",
            "sources": [ "src/native.cpp", "src/set.cpp", "src/iterator.cpp" ],
            "cflags": [ "-std=c++0x" ],
            "include_dirs" : [ "<!(node -e \"require('nan')\")" ]
    }]
}
