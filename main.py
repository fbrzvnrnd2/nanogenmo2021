from noise import pnoise1
from random import randint

maschio=pnoise1
femmina=pnoise1

sento=0
santo=0

capitolo=0
cambio=0
stato=0

amo_detto_fem=["Mi ami, piccolo?","Portami con te! Rapiscimi!… Te ne supplico!","Ti amo", "Oh! Ma è perché ti amo!", "Ti amo tanto da non poter vivere senza di te, capisci?", "Certe volte provo un tale desiderio di vederti che mi sento lacerare da tutte le furie dell'amore", " Sono la tua serva e la tua concubina! Tu sei il mio re, il mio idolo!", "Sei buono sei bello, sei intelligente, sei forte!","Quando suonerà mezzanotte penserai a me!", "Mi ami?", "Oh! Com'è buono lei!", "Potremmo andare a vivere altrove… in qualche luogo…", "Mi ami?", "Ti amo tanto da non poter vivere senza di te, capisci? Certe volte provo un tale desiderio di vederti che mi sento lacerare da tutte le furie dell'amore. Mi domando: dov'è in questo momento? Forse con altre donne? Gli sorridono, lui si avvicina… Oh, no, non è possibile, ce n'è qualcuna che ti piace? Lo so, ce ne sono di più belle di me; ma io so amarti meglio! Sono la tua serva e la tua concubina! Tu sei il mio re, il mio idolo! Sei buono sei bello, sei intelligente, sei forte!", "La cosa più tragica — non le sembra? — è dover trascinare, come faccio io, un'esistenza senza scopo. Se le nostre sofferenze potessero servire a qualcuno, ci si potrebbe consolare pensando all'utilità del sacrificio."]
amo_pens_fem=["Emma lo trovava attraente e non riusciva ad allontanare da lui i propri pensieri; ne ricordava gli atteggiamenti in altre occasioni, le frasi che aveva detto, il suono della voce e la figura; e ripeteva il suo nome, protendendo le labbra come per un bacio.", "'Sì, affascinante! Affascinante!… Amerà una donna? E chi?… Può amare soltanto me!' si domandava.", "Tra sé e sé pensava:'Oh! Se il Cielo lo avesse voluto! Perché non è successo? Chi lo ha impedito?…'", "Quanto più Emma si rendeva conto di essere innamorata, tanto più cercava di respingere questo amore, di diminuirlo, perché nessuno potesse accorgersene.", "Questo diede l'impressione a Emma che il loro grande amore, nel quale viveva immersa, stesse diminuendo sotto di lei come l'acqua di un fiume assorbita dal letto in cui scorre, ed ella cominciò a scorgere il fango.", "Emma si chinava verso l'amante e mormorava tra sé e sé, quasi soffocata dal languore: 'Oh! Non ti muovere! Non parlare! Guardami! C'è qualcosa di così dolce nei tuoi occhi, che mi fa un gran bene!'"]
amo_fatto_fem=[ "Nessun uomo le era parso più bello di Léon. Il suo contegno attestava uno squisito candore. Abbassò le lunghe ciglia sottili e incurvate.", "Emma, ansimante, si sentì cadere e per un attimo appoggiò il capo alla spalla di lui.", "Emma si abbandonò contro la parete e si coprì gli occhi con una mano.", "Lo guardava e sorrideva senza sapere il perché.", "Rimaneva affranta, ansimante, inerte, singhiozzando sommessamente e versando fiumi di lacrime.","Emma non aveva un aspetto allegro: gli angoli della bocca erano segnati da quelle pieghe amare che caratterizzano il viso delle anziane zitelle e degli ambiziosi decaduti.", "La signora Bovary riprese il braccio di Leon.", "La signora Bovary vedeva nei suoi occhi pagliuzze dorate intorno alle pupille nere e sentiva il profumo della pomata che gli rendeva lustri i capelli. Si sentì presa dal languore, ricordò il Visconte che le aveva fatto ballare il valzer alla Vaubyessard, la barba di lui, che emanava lo stesso profumo di vaniglia e di limone dei capelli di Leon, e, senza volerlo, socchiuse le palpebre per aspirarlo meglio.", "Emma si voltò verso di lui con un singhiozzo.", "'Oh, Leon!' sussurrò lentamente la giovane signora, abbandonandoglisi sulla spalla.", "Ella arrovesciò il collo candido, che un sospiro faceva palpitare, disfatta, in lacrime, con un lungo fremito, nascondendo il viso, e si abbandonò.", "Andava ripetendosi: «Ho un amante! Ho un amante!» e questa idea la deliziava come se le avessero promesso una seconda adolescenza."]
odio_detto_fem=["Perché, buon Dio, mi sono sposata?", "Ma hai perso la testa? Vuoi renderti ridicolo? Rimani a sedere.", "Oh! Mi fa paura Mi vuol fare del male? Andiamocene!", "Siediti. Mi dai ai nervi.", "Lasciami stare!", "Fuori!", "Taci, taci!", "Io sono troppo vecchia… Lei è troppo giovane… Mi dimentichi! Altre donne l'ameranno… e lei le ricambierà.", "Ma lei è pazzo! Lei è pazzo!", "Quanto sei vigliacco!"]
odio_pens_fem=["La conversazione di Leon era piatta come un marciapiede e le idee più comuni vi sfilavano nel loro abito di tutti i giorni, senza suscitare emozione o risate o fantasticherie.", "Leon era là, aveva il berretto calcato fin sulle sopracciglia, e le grosse labbra tremanti aggiungevano una nota di stupidità al suo viso; perfino la schiena, quella sua schiena tranquilla, riusciva a irritarla quando la guardava: le sembrava di vedervi spiegata sopra la finanziera tutta l'insulsaggine che lo caratterizzava.", "Emma si domandava come avesse potuto pensare che un uomo simile valesse qualcosa, quando già tante volte aveva avuto modo di rendersi conto della sua assoluta mediocrità.", "Emma rammentò tutte le sue aspirazioni a una vita lussuosa, le frustrazioni dell'anima sua, le meschinità del matrimonio, della vita di tutti i giorni, i sogni caduti nel fango come rondini ferite, i desideri, le rinunce, tutto quello che avrebbe potuto avere! E per che cosa? Per che cosa? Lo aveva fatto per lui, per questo individuo, per quest'uomo che non capiva niente, privo di ogni sensibilità.", "Lei aveva fatto di tutto per amarlo, e si era pentita, aveva pianto, per avere ceduto a un altro.", "Tutto di lui adesso la irritava, il viso, l'abito, quello che non diceva, il suo atteggiamento, la sua esistenza.", "La donna si pentiva, come di un delitto, della fedeltà di un tempo, e ciò ch'era rimasto della sua virtù crollava ormai sotto i colpi furiosi dell'orgoglio.", "Leon le appariva così distaccato ormai dalla sua vita, lontano per sempre, fuori della realtà e addirittura annientato come se stesse per morire, come se stesse agonizzando sotto i suoi stessi occhi.", "Leon non le era mai sembrato tanto sgradevole, con quelle dita quadrate, l'intelligenza ottusa, le maniere volgari.", "Le sembrava meschino, debole, una nullità, un pover'uomo in tutti i sensi." ,"Emma pensò: mi tradisca pure, che m'importa! Mi preme poi così tanto?", "Ogni sorriso nascondeva uno sbadiglio di noia, ogni gioia una maledizione, tutti i piaceri, il disgusto, e i baci più appassionati lasciavano sulla bocca soltanto l'irrealizzabile desiderio di una voluttà più grande."]
odio_fatto_fem=["L'umiliazione di Emma sentirsi debole si trasformava in un rancore mitigato soltanto dalla voluttà.", "Emma aveva quasi paura.", "Leon la soggiogava.", "Emma si mordeva le labbra livide e rigirava fra le dita un frammento di madrepora che aveva staccato, fissando su Leon sguardi infuocati, come frecce di fuoco pronte a trafiggerlo.", "Ricadde a sedere disperata.", "Lo sguardo di Emma cadde sul giovane, colmo di glaciale maestà", " Emma si passò la mano sul viso con un brivido.", "Accusava Léon delle proprie speranze deluse quasi l'avesse tradita, e arrivava ad augurarsi una catastrofe che avrebbe facilitato la loro separazione, dal momento che lei non trovava il coraggio di deciderla."] 
ind_detto_fem=["Lasciami, mi sciupi il vestito.", "Per me non esiste niente di più bello del sole al tramonto, soprattutto in riva al mare.","Detesto i personaggi comuni e i sentimenti moderati, come quelli che si incontrano nella realtà.", "Noi, povere donne, non possiamo permetterci simili distrazioni!", "Ma bisogna pure rispettare l'opinione della gente e obbedire alla morale.", "Mi dimenticherà, passerò come un'ombra.", "Ah! Senta, non ne parliamo più.", "Faccio male, faccio male! Sono pazza a darle retta", "Cos'è che ti turba? Dimmelo.", "Basta!", "Ah! Se tu volessi!…", "E non hai amato mai nessun'altra?", "Povero amico mio.", "Ebbene?…", "Che bambino! Via, dobbiamo essere saggi. Desidero così!", "Ah! Léon!… Veramente… io non so… se devo…", "È molto sconveniente, lo sa?", "Suvvia, va bene, ora vattene.", "Ah! un giorno mi lascerai!… Ti sposerai!… Sarai anche tu come gli altri.", "Siete tutti infami!", "'Eh!, no! E lo sa benissimo. È una cosa impossibile!'"]
ind_pens_fem=["Emma, evitava di domandarsi se lo amasse. Era convinta che l'amore dovesse arrivare di colpo, accompagnato da luci e fragori, simile a un uragano celeste che piomba sulla vita, la sconvolge, travolgendo la volontà come foglie secche, e trascina ogni sentimento nell'abisso.", "'Tanto non mi ama più', pensava.", "Emma pensò a Leon: era incapace di eroismo, debole, banale, più effeminato di una donna, avaro anche, e pusillanime.", "Era costretta a confessare di non provare niente di straordinario."]
ind_fatto_fem=["Si mossero uno verso l'altra: lui tese la mano, la signora Bovary esitò.", "Emma l'ascoltava a capo chino, smuovendo con la punta del piede le schegge di legno, per terra.", "Emma era in piedi; i grandi occhi ardenti lo guardavano seri e quasi terribili. Poi le lacrime li offuscarono, le palpebre rosate si abbassarono, abbandonò le mani e Léon stava per baciarle."]
desc_fem=["Emma portava una piccola cravatta di seta blu che teneva diritto, come una gorgiera, un colletto di batista pieghettato; a seconda dei movimenti del capo, il viso vi affondava o ne riemergeva dolcemente.", "Spesso Emma si fermava un istante per guardare dove metteva il piede e, vacillando sulla pietra malferma, con i gomiti sollevati, la figura inclinata e l'occhio indeciso, rideva della propria paura di cadere","Seduta nella poltrona vicino alla finestra, ella guardava passare sul marciapiede la gente del villaggio.","Dai capelli raccolti le scendeva sulle spalle una sfumatura scura che si andava man mano schiarendo, perdendosi infine nell'ombra. L'abito le ricadeva dai due lati della sedia, gonfio e pieno di pieghe, fino a terra. Quando Léon per caso si accorgeva di avervi posato sopra la suola di una scarpa, la ritirava in fretta come se avesse calpestato qualcosa di vivo."]

amo_desc_com=["Sentivano dentro di sé come un mormorio profondo, incessante, più forte delle loro stesse voci.", "I loro occhi erano colmi di una gravità degna di parole più serie, e, mentre si sforzavano di trovare frasi banali, si sentivano presi da uno stesso languore.", "Si guardarono: i loro pensieri, confusi nella medesima angoscia, sembravano stringersi in un abbraccio forte e palpitante."]

amo_fatto_masc=["Léon dietro a Emma che teneva il capo abbassato si chinò sul collo di lei e la baciò a lungo sulla nuca.","Léon declamava versi con una voce strascicata che diveniva diligentemente sospirosa nei punti in cui si parlava d'amore.", "Stava con le braccia incrociate sulle ginocchia e, levando il viso verso Emma, la guardava da vicino fissamente.", "Un unico desiderio faceva fremere a entrambi le labbra aride e, mollemente, senza sforzo, le loro dita si intrecciarono.", "Leon ricominciò a parlarle del suo amore per lei.", "Cercò di non impaurirla con complimenti audaci. Si mantenne calmo, serio, malinconico.", "Leon l'afferrò per il polso.", "Ridivenne di colpo rispettoso, carezzevole, timido. Le diede il braccio e si incamminarono sulla via del ritorno.", "Le circondò la vita con il braccio.", "Leon di tanto in tanto, si protendeva a prenderle la mano per baciarla.", "Leon aveva un gran mantello, l'avvolgeva tutta e, passandole un braccio intorno alla vita, la trascinava in silenzio fino in fondo alla stanza.", "Léon cercava la maniera di riannodare il dialogo interrotto.", "Léon sedeva sul pavimento, davanti a lei, appoggiava i gomiti sulle ginocchia, e la contemplava sorridendo e con il viso disteso."]
amo_detto_masc=["Immaginavo a volte che il caso l'avrebbe ricondotta a me. Ho creduto di riconoscerla agli angoli delle strade: e correvo accanto a tutte le carrozze dai cui finestrini svolazzasse una sciarpa, un velo simile al suo…", "Se ti amo! Se ti amo? Ma ti adoro, amore mio!", "Sia tanto buona da soddisfare almeno un mio capriccio.", "Io l'amo, ecco tutto! E lei lo sa bene! Mi dica una sola parola, una parola soltanto!", "Perdonami! Sei la sola che mi piaccia, sono stato imbecille e cattivo. Ti amo e ti amerò sempre.", "Eccomi di nuovo qui.", "Sì, ho sentito la mancanza di moltissime cose nella vita! Sono sempre stato solo! Ah! Avessi almeno uno scopo! Avessi incontrato un affetto, avessi avuto vicino qualcuno… Oh! Come avrei volentieri speso tutte le energie di cui sono capace, come avrei saputo sormontare ogni ostacolo, come sarei riuscito ad abbattere ogni barriera che impedisse il mio cammino!", "Cento volte sono stato deciso ad andarmene, ma, senza saperlo, la seguivo, e sono rimasto.", "Così come non me ne andrò stasera, domani, i giorni a venire, tutta la vita!", "Perché non ho mai trovato in nessuna donna un fascino irresistibile come quello che lei possiede", "Lei non mi respinge. Lei è buona, ha capito che io le appartengo! Mi permetta di guardarla, di contemplarla!", "Si, penso a lei senza posa… Il suo ricordo mi fa impazzire! Ah, mi perdoni!… È meglio che me ne vada... Addio!... Andrò lontano… così lontano che non sentirà più parlare di me!... Eppure, ancora adesso, non so quale forza mi abbia spinto verso di lei. Non si può lottare contro il Cielo, non si può resistere al sorriso degli angeli! Ci si lascia trascinare perché è bello, affascinante, adorabile!","La notte, tutte le notti, mi alzavo, arrivavo fin qui, guardavo la sua casa, il tetto che brillava sotto la luna, gli alberi del giardino che si dondolavano sotto la sua finestra, e una lampada fioca, un bagliore che splendeva al di là dei vetri, nell'ombra.", "I nostri destini son forse ormai uniti?", "Sono sicuro che lei si sbaglia. Non vuole convincersi che vive nella mia anima come una madonna, su un piedistallo ben alto, solido e immacolato. Ma ho bisogno di lei per vivere. Ho bisogno di guardare i suoi occhi, di ascoltare la sua voce, di sapere che qualche volta pensa a me. Perché non vuole essere mia amica, mia sorella, il mio angelo?", "Dammi un bacio, cara!", "Che cos'hai? Ma che cos'hai? Calmati, cerca di riprenderti! Sai che ti amo!… vieni!", "Non scherzi! Basta, basta per pietà! Mi permetta di rivederla… una volta… una sola."]
amo_pens_masc=["Leon si mise a pensare: 'Che pazzia! Come potevo illudermi di arrivare fino a lei?'", "Leon pensava. 'È molto carina la moglie del medico! Ha bei denti occhi neri, piedi minuscoli e una figuretta da parigina. Da dove diavolo è uscita, costei? E dove mai l'avrà trovata quel pezzo di malanno?'", "Leon si mise a riflettere: 'Ha occhi capaci di penetrare nel cuore come succhielli. E quella carnagione chiara! Io adoro le donne con la pelle chiara!'", "Emma era così carina! Léon ne aveva conosciute poche di un simile candore! Questo amore, non contaminato dal vizio, rappresentava per lui qualcosa di nuovo che, discostandosi dalle facili avventure cui era abituato, solleticava tanto il suo orgoglio quanto la sua sensualità."]
ind_fatto_masc=["Léon aveva posato un piede su un piolo della sedia sulla quale stava seduta la signora Bovary.","Si passò la mano sul viso, quasi si sentisse stordito, poi la lasciò cadere su quella di Emma, che la ritrasse.", "Leon taceva.", "L'uomo non le diceva più, come un tempo, quelle parole dolci che la facevano piangere, né aveva per lei quelle travolgenti carezze che la facevano impazzire di passione.", "Leon nascose sempre meno la propria indifferenza."]
ind_detto_masc=["Ebbene?…", "È necessario ridimensionare i discorsi esagerati che spesso nascondono sentimenti mediocri.", "È piacevole, in mezzo alle disillusioni della vita, poter rivolgere i propri pensieri su nobili figure, affetti puri e immagini di felicità.", "E io che cosa ci posso fare?", "Ma tu sei proprio pazza! Ti pare possibile?", "Ma sì ti amo!", "Pensi di avermi preso vergine?", "Via, povero angelo, coraggio, non te la prendere, abbi pazienza!", "Ho tanto sofferto! Spesso uscivo, me ne andavo, mi trascinavo sulle rive del fiume, mi stordivo al frastuono della folla senza riuscire a liberarmi dall'ossessione che mi perseguitava.", "Spesso le scrivevo e poi strappavo sempre le lettere.", "Non facciamoci vedere troppo presto, sarebbe un errore."]
ind_pens_masc=["Poiché labbra viziose o venali gli avevano mormorato frasi simili, non attribuiva molta importanza al candore di Emma.", "Leon pensò: 'Come mi annoio!'", "Leon aveva pensato: 'Se è vero che mi ha amato fin dal primo giorno, la smania di rivedermi farà sì che mi ami ancora di più! E allora andiamo avanti così'.", "Leon si era sentito dire tante volte tutte queste cose che ormai non avevano per lui più niente di originale. Emma non era diversa dalle altre amanti, e il fascino della novità, cadendo a poco a poco come un abito, metteva a nudo l'eterna monotonia della passione, che ha sempre le stesse forme e lo stesso linguaggio."]
odio_fatto_masc=["Sorridente e con una strana espressione sul viso, gli occhi fissi e i denti serrati, Leon avanzò verso di lei allargando le braccia.", "Leon si ribellava contro l'annullamento ogni giorno più grande della propria personalità.", "Nutriva rancore contro Emma per quella continua supremazia.", "Il giovane, riflettendo, si rese conto che l'amante si comportava in maniera strana, tanto da trovare ragionevoli coloro che cercavano di staccarlo da lei.", "Léon  aveva giurato che non avrebbe più rivisto Emma, e si rimproverava ora di non avere mantenuto la parola.", "Léon si sentiva infastidito adesso quando Emma d'improvviso si metteva a singhiozzare sul suo petto.", "Il cuore di lui, simile a quelle persone che si stancano se ascoltano per lungo tempo la musica, si assopiva nell'indifferenza alle manifestazioni clamorose di un amore del quale non apprezzava più le raffinatezze."]
odio_pens_masc=["Leon pensava che sarebbe stato meglio non incontrarla mai.", "V'era in quella fronte coperta da un sudore freddo sulle labbra balbettanti, nelle pupille smarrite, nella stretta delle braccia di Emma, qualcosa di estremo, di vago e di lugubre, che Léon sentiva insinuarsi fra loro, sottilmente, come se volesse separarli.", "Non osava porle domande; ma, vedendola così esperta, si era convinto che fosse dovuta passare attraverso tutte le prove della sofferenza e del piacere.", "Quello di Emma che un tempo lo aveva affascinato, adesso lo spaventava un poco. ", "Leon si sforzava di non amarla; poi, soltanto sentendo scricchiolare le sue scarpette, si sentiva privo di volontà, come un alcoolizzato alla vista dei liquori forti.", "Il giovane si sentì divenire debole sotto l'effetto della tacita volontà di quella donna che lo spingeva al crimine."]
odio_detto_masc=["Addio, allora!", "Sono stato molto occupato e anche indisposto.", "È un'insolente, una testa vuota! E forse peggio!", "Che imbecille sono mai! Non importa, era un'amante deliziosa!", "Ah, no, no, mille volte no! Sarebbe un errore madornale!", "Quante frottole!", "Ci sarebbe voluta qualche lacrima qui sopra; ma non riesco a piangere, non è colpa mia.!", "Imbecille!", "Sei pazza!"]
amo_fatto_due=["incominciavano allora a parlare a voce bassa e la conversazione sembrava più dolce perché nessuno l'ascoltava."]

while (stato<2000):
 stato=stato+1
 sento=sento+0.01
 santo=santo+0.01
 sentimentom=maschio(sento)
 if (sentimentom < -0.3):
  #print("***LUI ODIA LEI***")
  if (cambio != 1):
   capitolo=capitolo+1
   print ()
   print (capitolo)
   print ()
   cambio =1
  scelgo=randint(0,2)
  if (capitolo==2 or capitolo==12): #capitoli in cui parlano solo
   scelgo=0
  if (capitolo==3 or capitolo==13): #capitoli in cui agiscono solo
   scelgo=1
  if (capitolo==5 or capitolo==15): #capitoli in cui pensano solo
   scelgo=2      
  if (scelgo==0):
   print("Leon disse: "+odio_detto_masc[randint(0,len(odio_detto_masc)-1)])
  if (scelgo==1):
   print(odio_fatto_masc[randint(0,len(odio_fatto_masc)-1)])
  if (scelgo==2):
   print(odio_pens_masc[randint(0,len(odio_pens_masc)-1)]) 
 if (sentimentom > 0.2):
  #print("***LUI AMA LEI***")
  if (cambio != 2):
   capitolo=capitolo+1
   print ()
   print (capitolo)
   print ()
   cambio =2
  scelgo=randint(0,2)
  if (capitolo==2 or capitolo==12): #capitoli in cui parlano solo
   scelgo=0
  if (capitolo==3 or capitolo==13): #capitoli in cui agiscono solo
   scelgo=1
  if (capitolo==5 or capitolo==15): #capitoli in cui pensano solo
   scelgo=2
  if (scelgo==0):
   print("Leon disse: "+amo_detto_masc[randint(0,len(amo_detto_masc)-1)])
  if (scelgo==1):
   print(amo_fatto_masc[randint(0,len(amo_fatto_masc)-1)])
  if (scelgo==2):
   print(amo_pens_masc[randint(0,len(amo_pens_masc)-1)])
 if (sentimentom >= -0.3 and sentimentom <=0.2):
  #print("***LUI È INDIFFERENTE A LEI ***")
  if (cambio != 3):
   capitolo=capitolo+1
   print ()
   print (capitolo)
   print ()
   cambio =3
  scelgo=randint(0,2)
  if (capitolo==2 or capitolo==12): #capitoli in cui parlano solo
   scelgo=0
  if (capitolo==3 or capitolo==13): #capitoli in cui agiscono solo
   scelgo=1
  if (capitolo==5 or capitolo==15): #capitoli in cui pensano solo 
   scelgo=2
  if (scelgo==0):
   print("Leon disse: "+ind_detto_masc[randint(0,len(ind_detto_masc)-1)])
  if (scelgo==1):
   print(ind_fatto_masc[randint(0,len(ind_fatto_masc)-1)])
  if (scelgo==2):
   print(ind_pens_masc[randint(0,len(ind_pens_masc)-1)])
 
 sentimentof=femmina(santo)
 if (sentimentof < -0.3):
  #print("***LEI ODIA LUI***")
  scelgo=randint(0,2)
  if (capitolo==2 or capitolo==12): #capitoli in cui parlano solo
   scelgo=0
  if (capitolo==3 or capitolo==13): #capitoli in cui agiscono solo
   scelgo=1
  if (capitolo==5 or capitolo==15): #capitoli in cui pensano solo
   scelgo=2
  if (scelgo==0):
   print("Emma disse: "+odio_detto_fem[randint(0,len(odio_detto_fem)-1)])
  if (scelgo==1):
   print(odio_fatto_fem[randint(0,len(odio_fatto_fem)-1)])
  if (scelgo==2):
   print(odio_pens_fem[randint(0,len(odio_pens_fem)-1)]) 
 if (sentimentof > 0.2):
  #print("***LEI AMA LUI***")
  scelgo=randint(0,2)
  if (capitolo==2 or capitolo==12): #capitoli in cui parlano solo
   scelgo=0
  if (capitolo==3 or capitolo==13): #capitoli in cui agiscono solo
   scelgo=1
  if (capitolo==5 or capitolo==15): #capitoli in cui pensano solo
   scelgo =2
  if (scelgo==0):
   print("Emma disse: "+amo_detto_fem[randint(0,len(amo_detto_fem)-1)])
  if (scelgo==1):
   print(amo_fatto_fem[randint(0,len(amo_fatto_fem)-1)])
  if (scelgo==2):
   print(amo_pens_fem[randint(0,len(amo_pens_fem)-1)])
 if (sentimentof >= -0.3 and sentimentof <=0.2):
  #print("***LEI È INDIFFERENTE A LUI***")
  scelgo=randint(0,2)
  if (capitolo==2 or capitolo==12): #capitoli in cui parlano solo
   scelgo=0
  if (capitolo==3 or capitolo==13): #capitoli in cui agiscono solo
   scelgo=1
  if (capitolo==5 or capitolo==15): #capitoli in cui pensano solo
   scelgo=2
  if (scelgo==0):
   print("Emma disse: "+ind_detto_fem[randint(0,len(ind_detto_fem)-1)])
  if (scelgo==1):
   print(ind_fatto_fem[randint(0,len(ind_fatto_fem)-1)])
  if (scelgo==2):
   print(ind_pens_fem[randint(0,len(ind_pens_fem)-1)])