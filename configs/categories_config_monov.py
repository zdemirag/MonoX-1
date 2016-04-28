# Configuration for a simple monojet topology. Use this as a template for your own Run-2 mono-X analysis
# First provide ouput file name in out_file_name field 

out_file_name = 'mono-x.root'
#bins = [250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 1000.0]
#bins = [250.0, 300.0, 350.0, 400.0, 450.0, 500.0, 550.0, 600.0, 800.0, 1000.0]
#bins = [250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 800.0, 1000.0]
#bins = [250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 700.0, 800.0, 1000.0]

bins = [250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0]


monojet_category = {
	    'name':"monojet"
            #,'in_file_name':"/afs/cern.ch/work/d/dabercro/public/Winter15/MonoX/monojet/plotter/limits/160222/MonoVLimitsTrees.root"
            ,'in_file_name':"/afs/cern.ch/work/d/dabercro/public/Winter15/MonoX/monojet/analysis/limits/160311/MonoVLimitsTrees.root"
            ,"cutstring":"met>200"
            ,"varstring":["met",250,1000]
            ,"weightname":"scaleMC_w"
            ,"bins":bins[:]
            ,"additionalvars":[['met',100,200,1000]]
            ,"pdfmodel":0
            ,"samples":
	   	{  
		  # Signal Region
                   "Zvv_ht100_signal"              :['signal','zjets',1,0]
                  ,"Zvv_ht200_signal"              :['signal','zjets',1,0]
                  ,"Zvv_ht400_signal"              :['signal','zjets',1,0]
                  ,"Zvv_ht600_signal"              :['signal','zjets',1,0]
                  ,"Zll_ht100_signal"              :['signal','zll',1,0]
                  ,"Zll_ht200_signal"              :['signal','zll',1,0]
                  ,"Zll_ht400_signal"              :['signal','zll',1,0]
                  ,"Zll_ht600_signal"              :['signal','zll',1,0]                   
                  ,"Wlv_ht100_signal"              :['signal','wjets',1,0]
                  ,"Wlv_ht200_signal"              :['signal','wjets',1,0]
                  ,"Wlv_ht400_signal"              :['signal','wjets',1,0]
                  ,"Wlv_ht600_signal"              :['signal','wjets',1,0]
                  ,"Wlv_ht800_signal"              :['signal','wjets',1,0]
                  ,"Wlv_ht1200_signal"             :['signal','wjets',1,0]
                  ,"Wlv_ht2500_signal"             :['signal','wjets',1,0]
                  ,"others_signal"                 :['signal','top',1,0]
                  ,"antitop_signal"                :['signal','top',1,0]
                  ,"antitop_5f_signal"             :['signal','top',1,0]
                  ,"top_signal"                    :['signal','top',1,0]
                  ,"top_5f_signal"                 :['signal','top',1,0]
                  ,"QCD_200To300_signal"           :['signal','qcd',1,0]
                  ,"QCD_300To500_signal"           :['signal','qcd',1,0]
                  ,"QCD_500To700_signal"           :['signal','qcd',1,0]
                  ,"QCD_700To1000_signal"          :['signal','qcd',1,0]
                  ,"QCD_1000To1500_signal"         :['signal','qcd',1,0]
                  ,"GJets_100To200_signal"         :['signal','gjets',1,0]
                  ,"GJets_200To400_signal"         :['signal','gjets',1,0]
                  ,"GJets_400To600_signal"         :['signal','gjets',1,0]
                  ,"GJets_600ToInf_signal"         :['signal','gjets',1,0]
                  ,"WW_signal"                     :['signal','diboson',1,0]
                  ,"WZ_signal"                     :['signal','diboson',1,0]
                  ,"ZZ_signal"                     :['signal','diboson',1,0]                  
                  ,"data_signal"                   :['signal','data',0,0]
                  ,"signal_h125_ggf_signal"                :['signal','higgs125ggf',1,1]
                  ,"signal_h125_vbf_signal"                :['signal','higgs125vbf',1,1]
                  ,"signal_wh125_signal"                   :['signal','higgs125wh',1,1]
                  ,"signal_zh125_signal"                   :['signal','higgs125zh',1,1]
                  ,"Pseudoscalar_Mphi-500_Mchi-10_signal"  :['signal','ps500_10',1,1]
                  ,"Pseudoscalar_Mphi-500_Mchi-150_signal" :['signal','ps500_150',1,1]
                  ,"Pseudoscalar_Mphi-500_Mchi-1_signal"   :['signal','ps500_1',1,1]
                  ,"Scalar_Mphi-500_Mchi-10_signal"        :['signal','s500_10',1,1]
                  ,"Scalar_Mphi-500_Mchi-150_signal"       :['signal','s500_150',1,1]
                  ,"Scalar_Mphi-500_Mchi-1_signal"         :['signal','s500_1',1,1]  
                  ,"Axial_Mphi-500_Mchi-1_signal"          :['signal','av500_1',1,1]
                  ,"Axial_Mphi-2000_Mchi-100_signal"       :['signal','av2000_100',1,1]
                  ,"Axial_Mphi-2000_Mchi-150_signal"       :['signal','av2000_150',1,1]
                  ,"Axial_Mphi-2000_Mchi-1_signal"         :['signal','av2000_1',1,1]
                  ,"Vector_Mphi-2000_Mchi-100_signal"      :['signal','v2000_100',1,1]
                  ,"Vector_Mphi-2000_Mchi-10_signal"       :['signal','v2000_10',1,1]
                  ,"Vector_Mphi-2000_Mchi-50_signal"       :['signal','v2000_50',1,1]
                  ,"VectorMonoZ_Mphi-2000_Mchi-10_signal"  :['signal','monoz_v2000_10',1,1]
                  ,"VectorMonoW_Mphi-2000_Mchi-10_signal"  :['signal','monow_v2000_10',1,1]
                  ,"AxialMonoZ_Mphi-500_Mchi-1_signal"     :['signal','monoz_av500_1',1,1]
                  ,"AxialMonoW_Mphi-500_Mchi-1_signal"     :['signal','monow_av500_1',1,1]

                  # Dimuon Control Region
                  ,"Zll_ht100_Zmm"              :['Zmm','zll',1,1]
                  ,"Zll_ht200_Zmm"              :['Zmm','zll',1,1]
                  ,"Zll_ht400_Zmm"              :['Zmm','zll',1,1]
                  ,"Zll_ht600_Zmm"              :['Zmm','zll',1,1]
                  ,"others_Zmm"                 :['Zmm','top',1,0]
                  ,"antitop_Zmm"                :['Zmm','top',1,0]
                  ,"antitop_5f_Zmm"             :['Zmm','top',1,0]
                  ,"top_Zmm"                    :['Zmm','top',1,0]
                  ,"top_5f_Zmm"                 :['Zmm','top',1,0]
                  ,"WW_Zmm"                     :['Zmm','diboson',1,0]
                  ,"WZ_Zmm"                     :['Zmm','diboson',1,0]
                  ,"ZZ_Zmm"                     :['Zmm','diboson',1,0]
                  ,"data_Zmm"                   :['Zmm','data',0,0]

                  # Dielectron Control Region
                  ,"Zll_ht100_Zee"              :['Zee','zll',1,1]
                  ,"Zll_ht200_Zee"              :['Zee','zll',1,1]
                  ,"Zll_ht400_Zee"              :['Zee','zll',1,1]
                  ,"Zll_ht600_Zee"              :['Zee','zll',1,1]
                  ,"others_Zee"                 :['Zee','top',1,0]
                  ,"WW_Zee"                     :['Zee','diboson',1,0]
                  ,"WZ_Zee"                     :['Zee','diboson',1,0]
                  ,"ZZ_Zee"                     :['Zee','diboson',1,0]
                  ,"data_Zee"                   :['Zee','data',0,0]

                  # Single muon-Control
                  ,"Wlv_ht100_Wmn"              :['Wmn','wjets',1,1]
                  ,"Wlv_ht200_Wmn"              :['Wmn','wjets',1,1]
                  ,"Wlv_ht400_Wmn"              :['Wmn','wjets',1,1]
                  ,"Wlv_ht600_Wmn"              :['Wmn','wjets',1,1]
                  ,"Wlv_ht800_Wmn"              :['Wmn','wjets',1,1]
                  ,"Wlv_ht1200_Wmn"             :['Wmn','wjets',1,1]
                  ,"Wlv_ht2500_Wmn"             :['Wmn','wjets',1,1]
                  ,"Zll_ht100_Wmn"              :['Wmn','zll',1,0]
                  ,"Zll_ht200_Wmn"              :['Wmn','zll',1,0]
                  ,"Zll_ht400_Wmn"              :['Wmn','zll',1,0]
                  ,"Zll_ht600_Wmn"              :['Wmn','zll',1,0]                   
                  ,"others_Wmn"                 :['Wmn','top',1,0]
                  ,"antitop_Wmn"                :['Wmn','top',1,0]
                  ,"antitop_5f_Wmn"             :['Wmn','top',1,0]
                  ,"top_Wmn"                    :['Wmn','top',1,0]
                  ,"top_5f_Wmn"                 :['Wmn','top',1,0]
                  ,"QCD_200To300_Wmn"           :['Wmn','qcd',1,0]
                  ,"QCD_300To500_Wmn"           :['Wmn','qcd',1,0]
                  ,"QCD_500To700_Wmn"           :['Wmn','qcd',1,0]
                  ,"QCD_700To1000_Wmn"          :['Wmn','qcd',1,0]
                  ,"QCD_1000To1500_Wmn"         :['Wmn','qcd',1,0]
                  ,"WW_Wmn"                     :['Wmn','diboson',1,0]
                  ,"WZ_Wmn"                     :['Wmn','diboson',1,0]
                  ,"ZZ_Wmn"                     :['Wmn','diboson',1,0]
                  ,"data_Wmn"                   :['Wmn','data',0,0]

                  # Single electron-Control
                  ,"Wlv_ht100_Wen"              :['Wen','wjets',1,1]
                  ,"Wlv_ht200_Wen"              :['Wen','wjets',1,1]
                  ,"Wlv_ht400_Wen"              :['Wen','wjets',1,1]
                  ,"Wlv_ht600_Wen"              :['Wen','wjets',1,1]
                  ,"Wlv_ht800_Wen"              :['Wen','wjets',1,1]
                  ,"Wlv_ht1200_Wen"             :['Wen','wjets',1,1]
                  ,"Wlv_ht2500_Wen"             :['Wen','wjets',1,1]
                  ,"Zll_ht100_Wen"              :['Wen','zll',1,0]
                  ,"Zll_ht200_Wen"              :['Wen','zll',1,0]
                  ,"Zll_ht400_Wen"              :['Wen','zll',1,0]
                  ,"Zll_ht600_Wen"              :['Wen','zll',1,0]
                  ,"others_Wen"                 :['Wen','top',1,0]
                  ,"antitop_Wen"                :['Wen','top',1,0]
                  ,"antitop_5f_Wen"             :['Wen','top',1,0]
                  ,"top_Wen"                    :['Wen','top',1,0]
                  ,"top_5f_Wen"                 :['Wen','top',1,0]
                  ,"QCD_200To300_Wen"           :['Wen','qcd',1,0]
                  ,"QCD_300To500_Wen"           :['Wen','qcd',1,0]
                  ,"QCD_500To700_Wen"           :['Wen','qcd',1,0]
                  ,"QCD_700To1000_Wen"          :['Wen','qcd',1,0]
                  ,"QCD_1000To1500_Wen"         :['Wen','qcd',1,0]
                  ,"WW_Wen"                     :['Wen','diboson',1,0]
                  ,"WZ_Wen"                     :['Wen','diboson',1,0]
                  ,"ZZ_Wen"                     :['Wen','diboson',1,0]
                  ,"data_Wen"                   :['Wen','data',0,0]
                   
                  # photon control region
                  ,"QCD_40To100_gjets"         :['gjets','qcd',1,0]
                  ,"QCD_100To200_gjets"        :['gjets','qcd',1,0]
                  ,"QCD_200To400_gjets"        :['gjets','qcd',1,0]
                  ,"QCD_400To600_gjets"        :['gjets','qcd',1,0]
                  ,"QCD_600ToInf_gjets"        :['gjets','qcd',1,0]
                  
                  #,"QCD_200To300_gjets"          :['gjets','qcd',1,0]  
                  #,"QCD_300To500_gjets"          :['gjets','qcd',1,0]
                  #,"QCD_500To700_gjets"          :['gjets','qcd',1,0]
                  #,"QCD_700To1000_gjets"         :['gjets','qcd',1,0]
                  #,"QCD_1000To1500_gjets"        :['gjets','qcd',1,0]
                  ,"GJets_100To200_gjets"        :['gjets','gjets',1,1]
                  ,"GJets_200To400_gjets"        :['gjets','gjets',1,1]
                  ,"GJets_400To600_gjets"        :['gjets','gjets',1,1]
                  ,"GJets_600ToInf_gjets"        :['gjets','gjets',1,1]
                  ,"data_gjets"                  :['gjets','data',0,0]

	   	},
}
categories = [monojet_category]
