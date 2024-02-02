#ifndef _DLL_H_
#define _DLL_H_

#if BUILDING_DLL
#define DLLIMPORT __declspec(dllexport)
#else
#define DLLIMPORT __declspec(dllimport)
#endif

DLLIMPORT void HelloWorld();
DLLIMPORT int suma(int,int);
DLLIMPORT int resta(int,int);
#endif
