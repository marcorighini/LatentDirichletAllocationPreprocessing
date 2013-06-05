'''

@author: marco
'''
import  os, math, random

############## PREPROCESSING FOR DATASET ###################

def createKFold(args):
    if os.path.exists(args.corpus) == True and os.path.isdir(args.corpus) == False:
        if os.path.exists(args.vocabulary) == True and os.path.isdir(args.vocabulary) == False:
            
            if args.debug == True:
                print "> " + str(args)
                
            # Create data structures
            print ""
            print "> Parsing corpus..."
            
            # Create dicts for vocabulary (with ids as key and with words as keys)
            voc = {'id':{}, 'w':{}}
            vocabulary = open(args.vocabulary, 'r')
            for i, line in enumerate(vocabulary):
                line = line.rstrip('\n')
                identifier = i + 1
                voc['w'][line] = identifier
                voc['id'][identifier] = line
            vocabulary.close()
            
            # Create dict for dataset 
            dat = {}
            dataset = open(args.corpus, 'r')
            for i, line in enumerate(dataset):
                if i > 2:
                    line = line.split()
                    for n in range(int(line[2])):
                        dat.setdefault(int(line[0]), []).append(voc['id'][int(line[1])])
                       
            # Shuffle doc ids to randomize testset choice 
            docIds=dat.keys();
            print ">> Documents: "+str(len(docIds))
            random.shuffle(docIds)

            # Compute testset size            
            testSize=int(args.test_frac*len(docIds))
            
            testset={}
            for i in range(0,testSize):
                id=docIds[i]
                testset[id]=dat[id]
                del docIds[i]
                
            print ">> Testset documents: "+str(len(testset))
            
            # Compute folds
            print ">> Creating "+str(args.k)+" folds..."
            folds={}
            for i in range(0,args.k):
                folds[i]={}
            for i in range(0,len(docIds)):
                id=docIds[i]
                folds[i%args.k][id]=dat[id]
            
            for i in folds:
                print ">>> Documents in fold "+str(i)+": "+str(len(folds[i].keys()))
                
            # Compute datasets (training-validation couples)
            dataset={}
            if args.k==1:
                dataset[0]={'train':folds[0],'validation':{}}
            else:
                for i in range(0,args.k):
                    dataset[i]={'train':{},'validation':folds[i]}
                    m=range(0,args.k)
                    del m[i]
                    z={}
                    for k in m:
                        z.update(folds[k])
                    dataset[i]['train']=z
                    
            # # Write data
            if args.output == None:
                args.output = os.path.dirname(args.corpus)
            if os.path.isdir(args.output) == False:
                print "ERROR: Output directory not valid: " + args.output
            else:
                basename = args.output + "/" + os.path.splitext(os.path.basename(args.corpus))[0]
                
                # Write testset if created
                if len(testset.keys()) != 0:
                    testOutTxt = open(basename + "_test.dat", 'w')
                    testOutTxt.write(str(len(testset.keys())) + "\n")
                    for key in testset.keys():
                        wList = testset[key]
                        for i, word in enumerate(wList):
                            testOutTxt.write(word)
                            if i == len(wList) - 1:
                                testOutTxt.write("\n")
                            else:
                                testOutTxt.write(" ")
                    testOutTxt.close()
                    print ">> Testset created"
                    
                # Write training e validation
                for k in dataset.keys():
                    trainOutTxt = open(basename + "_"+str(k)+".dat", 'w')
                    trainOutTxt.write(str(len(dataset[k]['train'].keys())) + "\n")
                    for d in dataset[k]['train'].keys():
                        wList = dataset[k]['train'][d]
                        for i, word in enumerate(wList):
                            trainOutTxt.write(word)
                            if i == len(wList) - 1:
                                trainOutTxt.write("\n")
                            else:
                                trainOutTxt.write(" ")
                    trainOutTxt.close
                    
                    if len(dataset[k]['validation'].keys()) != 0:
                        validationOutTxt = open(basename + "_"+str(k)+"_val.dat", 'w')
                        validationOutTxt.write(str(len(dataset[k]['validation'].keys())) + "\n")
                        for d in dataset[k]['validation'].keys():
                            wList = dataset[k]['validation'][d]
                            for i, word in enumerate(wList):
                                validationOutTxt.write(word)
                                if i == len(wList) - 1:
                                    validationOutTxt.write("\n")
                                else:
                                    validationOutTxt.write(" ")
                        validationOutTxt.close
                    
                    print ">> Training-validation set #"+str(k)+" created"
        else:
            print "ERROR: Vocabulary path not valid: " + args.vocabulary
    else:
        print "ERROR: Corpus path not valid: " + args.corpus
        
####################### PREPROCESSING FOR VOCABULARY ###############################

def createVocabulary(datasetPath):
    # # Read dataset words and add to vocabulary
    dataset = open(datasetPath, 'r')
    voc = {}
    for i, line in enumerate(dataset):
            if i > 0:
                line = line.split()
                for w in line:
                    voc[w]=True
    dataset.close()
    keys=voc.keys()
    keys.sort()

    # # Write vocabulary
    outputPath = os.path.dirname(datasetPath)
    basename = outputPath + "/" + os.path.splitext(os.path.basename(datasetPath))[0]
    vocOut = open(basename + "_voc.dat", 'w')
    for w in keys:
        vocOut.write(w + "\n")
    vocOut.close()
    
    # # Return vocabulary reference dicts
    voc = {'id':{},'w':{}}
    for i,w in enumerate(keys):
        voc['id'][i]=w
        voc['w'][w]=i
    
    return voc
