import requests
from bs4 import BeautifulSoup
import csv

# List of Target URLs
urls = ['https://m.twitch.tv/kingsleague/about', 
'https://m.twitch.tv/BALLERLEAGUE/about', 
'https://m.twitch.tv/gerardromero/about', 
'https://m.twitch.tv/oestagiario/about', 
'https://m.twitch.tv/ElChiringuitoTV/about', 
'https://m.twitch.tv/sirolopez56/about', 
'https://m.twitch.tv/rubenmartinweb/about', 
'https://m.twitch.tv/tvplay_it/about', 
'https://m.twitch.tv/footballbromance/about', 
'https://m.twitch.tv/Diario_AS/about', 
'https://m.twitch.tv/elyihi/about', 
'https://m.twitch.tv/kingsleagueamericas/about', 
'https://m.twitch.tv/chiringuitoresubidos/about', 
'https://m.twitch.tv/BostonWEEI/about', 
'https://m.twitch.tv/WinamaxSport/about', 
'https://m.twitch.tv/kurt0411/about', 
'https://m.twitch.tv/ControCalcio__/about', 
'https://m.twitch.tv/diariooleok/about', 
'https://m.twitch.tv/valentisanjuan/about', 
'https://m.twitch.tv/CazeTV_/about', 
'https://m.twitch.tv/TheSportsLeader/about', 
'https://m.twitch.tv/SoyMotor/about', 
'https://m.twitch.tv/Chicago670thescore/about', 
'https://m.twitch.tv/DiarioMARCA/about', 
'https://m.twitch.tv/Juventibus/about', 
'https://m.twitch.tv/SantiZap/about', 
'https://m.twitch.tv/TeleRadioStereo/about', 
'https://m.twitch.tv/INAKIANGULOTV/about', 
'https://m.twitch.tv/Futbol_Fantasy/about', 
'https://m.twitch.tv/RetesportTV/about', 
'https://m.twitch.tv/teladoiotokyo/about', 
'https://m.twitch.tv/AmalaTV/about', 
'https://m.twitch.tv/AssodiRoma_Official/about', 
'https://m.twitch.tv/mundodeportivo/about', 
'https://m.twitch.tv/CALCIOBERLIN/about', 
'https://m.twitch.tv/agorafutbol/about', 
'https://m.twitch.tv/backyardbreaks/about', 
'https://m.twitch.tv/iaguirregabiria/about', 
'https://m.twitch.tv/RMCsport/about', 
'https://m.twitch.tv/senen98/about', 
'https://m.twitch.tv/radiosei98100/about', 
'https://m.twitch.tv/PoneeeyClub/about', 
'https://m.twitch.tv/Fantacalcio/about', 
'https://m.twitch.tv/Juakynen/about', 
'https://m.twitch.tv/LosFutbolitos/about', 
'https://m.twitch.tv/MiguelAngelRomanTV/about', 
'https://m.twitch.tv/TrashTalkFr/about', 
'https://m.twitch.tv/LaMediaInglesa/about', 
'https://m.twitch.tv/rubenuria_/about', 
'https://m.twitch.tv/GxlDePaulinho/about', 
'https://m.twitch.tv/SLAKUN10/about', 
'https://m.twitch.tv/elbermu93/about', 
'https://m.twitch.tv/LaGradaSports/about', 
'https://m.twitch.tv/tiempodejuegocope/about', 
'https://m.twitch.tv/AltitudeSR/about', 
'https://m.twitch.tv/Mundomaldini/about', 
'https://m.twitch.tv/Alvini98/about', 
'https://m.twitch.tv/BoboTvChannel/about', 
'https://m.twitch.tv/telemetropanama/about', 
'https://m.twitch.tv/soldadodeltenis/about', 
'https://m.twitch.tv/xbuyeroficial/about', 
'https://m.twitch.tv/masl_soccer/about', 
'https://m.twitch.tv/IvZel96/about', 
'https://m.twitch.tv/dallasfancam/about', 
'https://m.twitch.tv/fcinter1908_official/about', 
'https://m.twitch.tv/chiringuitodiirectos/about', 
'https://m.twitch.tv/TheGamblingCabin/about', 
'https://m.twitch.tv/PassioneFiorentina/about', 
'https://m.twitch.tv/GolTelevision/about', 
'https://m.twitch.tv/AdriContreras4/about', 
'https://m.twitch.tv/SPONTENT/about', 
'https://m.twitch.tv/PuntoDeportivoTV/about', 
'https://m.twitch.tv/FailArmy/about', 
'https://m.twitch.tv/PadelTVOfficial/about', 
'https://m.twitch.tv/JoseCarrasco_98/about', 
'https://m.twitch.tv/CAMP_NOU_NOW/about', 
'https://m.twitch.tv/PlanetaNBA/about', 
'https://m.twitch.tv/nanosecso/about', 
'https://m.twitch.tv/VictorAbadG/about', 
'https://m.twitch.tv/AJGtv/about', 
'https://m.twitch.tv/CentroSuonoSport1015/about', 
'https://m.twitch.tv/BritishBasketball/about', 
'https://m.twitch.tv/GetWin_Sport/about', 
'https://m.twitch.tv/Rodriguez/about', 
'https://m.twitch.tv/LeoDickinsonSumo/about', 
'https://m.twitch.tv/espn975/about', 
'https://m.twitch.tv/beisbolnegritoo/about', 
'https://m.twitch.tv/TNTSportsBr/about', 
'https://m.twitch.tv/LaytonSportsCards/about', 
'https://m.twitch.tv/BarcaHoy/about', 
'https://m.twitch.tv/slivooo/about', 
'https://m.twitch.tv/ElTronoKL/about', 
'https://m.twitch.tv/En3rix_/about', 
'https://m.twitch.tv/generaldepie/about', 
'https://m.twitch.tv/RobertoChinchero/about', 
'https://m.twitch.tv/masl_soccer2/about', 
'https://m.twitch.tv/BetBar_/about', 
'https://m.twitch.tv/LaGrada914/about', 
'https://m.twitch.tv/javierdeharo1961/about', 
'https://m.twitch.tv/緯來體育台官方頻道 (vlsportofficial)/about', 
'https://m.twitch.tv/elchiringuitodejugon1/about', 
'https://m.twitch.tv/HomeofHandball/about', 
'https://m.twitch.tv/TheFifaFinisher/about', 
'https://m.twitch.tv/RealMadrid/about', 
'https://m.twitch.tv/WinnersBeachVolleyball_1/about', 
'https://m.twitch.tv/GooFyLaLf/about', 
'https://m.twitch.tv/spidercarp23/about', 
'https://m.twitch.tv/betql/about', 
'https://m.twitch.tv/BryanBrosGolf/about', 
'https://m.twitch.tv/lefrenchiie/about', 
'https://m.twitch.tv/AnaOnAir/about', 
'https://m.twitch.tv/livefootballsims/about', 
'https://m.twitch.tv/ElIngenieroPedro/about', 
'https://m.twitch.tv/joanpradells/about', 
'https://m.twitch.tv/ByDiegoX10/about', 
'https://m.twitch.tv/SalvaGarciaJ/about', 
'https://m.twitch.tv/btvesports/about', 
'https://m.twitch.tv/CH14/about', 
'https://m.twitch.tv/Naranjazos/about', 
'https://m.twitch.tv/ATK_GAMIING/about', 
'https://m.twitch.tv/ElQuintoGrande/about', 
'https://m.twitch.tv/Depielo/about', 
'https://m.twitch.tv/FranceRugby/about', 
'https://m.twitch.tv/MilanNewsit/about', 
'https://m.twitch.tv/dj_ansi/about', 
'https://m.twitch.tv/CachorrosFB/about', 
'https://m.twitch.tv/apiedepuerto/about', 
'https://m.twitch.tv/中信兄弟官方頻道 (brothers_baseball)/about', 
'https://m.twitch.tv/inter/about', 
'https://m.twitch.tv/pushdich_tcg/about', 
'https://m.twitch.tv/marmita_sports/about', 
'https://m.twitch.tv/Studio_All_In/about', 
'https://m.twitch.tv/OMofficial/about', 
'https://m.twitch.tv/CerebroCule/about', 
'https://m.twitch.tv/elapostadorcol/about', 
'https://m.twitch.tv/NikoTB_/about', 
'https://m.twitch.tv/da_2bros1break/about', 
'https://m.twitch.tv/JoeKingPR21/about', 
'https://m.twitch.tv/Diariovasco/about', 
'https://m.twitch.tv/VortexSportscards/about', 
'https://m.twitch.tv/wheezyblonde/about', 
'https://m.twitch.tv/aPartidoUnico/about', 
'https://m.twitch.tv/LiveBianconera/about', 
'https://m.twitch.tv/BAMFBreakers/about', 
'https://m.twitch.tv/SocialGamblers/about', 
'https://m.twitch.tv/danibet_/about', 
'https://m.twitch.tv/PapaBuyer/about', 
'https://m.twitch.tv/luigiwrestling/about', 
'https://m.twitch.tv/WinnersGoalProCup/about', 
'https://m.twitch.tv/MARIAGMC_/about', 
'https://m.twitch.tv/CuseSportsTalk/about', 
'https://m.twitch.tv/JuveEdjogo/about', 
'https://m.twitch.tv/ColgadisimosDelAro/about', 
'https://m.twitch.tv/playon30/about', 
'https://m.twitch.tv/ikercasillas/about', 
'https://m.twitch.tv/HeelJosh/about', 
'https://m.twitch.tv/HerrFloeter/about', 
'https://m.twitch.tv/CBCsportscards/about', 
'https://m.twitch.tv/masl_soccer3/about', 
'https://m.twitch.tv/StadiumLiveApp/about', 
'https://m.twitch.tv/thibaudvezirian/about', 
'https://m.twitch.tv/la_fiera_del_calcio/about', 
'https://m.twitch.tv/doctorjota163/about', 
'https://m.twitch.tv/jugonesinside/about', 
'https://m.twitch.tv/dobbtvlive/about', 
'https://m.twitch.tv/MARCAvalladolid/about', 
'https://m.twitch.tv/SOSFantaLive/about', 
'https://m.twitch.tv/fedandfut/about', 
'https://m.twitch.tv/TheGodFlores/about', 
'https://m.twitch.tv/kapsel_hd/about', 
'https://m.twitch.tv/PSG/about', 
'https://m.twitch.tv/Sergioyco/about', 
'https://m.twitch.tv/RambleNow/about', 
'https://m.twitch.tv/koyotitospa/about', 
'https://m.twitch.tv/TheChiseledAdonis/about', 
'https://m.twitch.tv/territorioblaugrana/about', 
'https://m.twitch.tv/ibrahimoviktv/about', 
'https://m.twitch.tv/javibridgee/about', 
'https://m.twitch.tv/livedrivestream/about', 
'https://m.twitch.tv/Ubietoo/about', 
'https://m.twitch.tv/富邦悍將官方頻道 (fubonguardians_official)/about', 
'https://m.twitch.tv/MillerandMoulton/about', 
'https://m.twitch.tv/UltimateAutographs/about', 
'https://m.twitch.tv/CanalSupporters/about', 
'https://m.twitch.tv/FoosballTV/about', 
'https://m.twitch.tv/Marshalada/about', 
'https://m.twitch.tv/MaxKruseGaming/about', 
'https://m.twitch.tv/prideofdetroit/about', 
'https://m.twitch.tv/heataomilgrau/about', 
'https://m.twitch.tv/easyCreditBBL/about', 
'https://m.twitch.tv/DA_TheLiveLounge/about', 
'https://m.twitch.tv/thenexus123/about', 
'https://m.twitch.tv/HornATX/about', 
'https://m.twitch.tv/Conman167/about', 
'https://m.twitch.tv/TNTSportsAR/about', 
'https://m.twitch.tv/firstteam101/about', 
'https://m.twitch.tv/mmaseasonpodcast/about', 
'https://m.twitch.tv/JozaoFutebol/about', 
'https://m.twitch.tv/getsportsstream/about', 
'https://m.twitch.tv/fersports/about', 
'https://m.twitch.tv/JeFFF/about', 
'https://m.twitch.tv/il_tinca/about', 
'https://m.twitch.tv/madridismoaldia/about', 
'https://m.twitch.tv/La_Oposicion/about', 
'https://m.twitch.tv/LaMatinaleFoot/about', 
'https://m.twitch.tv/Challenger_Series/about', 
'https://m.twitch.tv/micheleposa/about', 
'https://m.twitch.tv/JoshODeezy/about', 
'https://m.twitch.tv/FABRIGARCIA517/about', 
'https://m.twitch.tv/AlexDandi_MMA/about', 
'https://m.twitch.tv/FutbolerosTV/about', 
'https://m.twitch.tv/petkus_tv/about', 
'https://m.twitch.tv/TQHTPodcast/about', 
'https://m.twitch.tv/maqwelll/about', 
'https://m.twitch.tv/pepponetwitch/about', 
'https://m.twitch.tv/SoWhat/about', 
'https://m.twitch.tv/GermanGarmendia/about', 
'https://m.twitch.tv/ElDesmarque_TV/about', 
'https://m.twitch.tv/JakeTv72/about', 
'https://m.twitch.tv/Atletico_Stats/about', 
'https://m.twitch.tv/alexandre_khaldi/about', 
'https://m.twitch.tv/manucolchon/about', 
'https://m.twitch.tv/GrittyUrbanSaga/about', 
'https://m.twitch.tv/jefezhai/about', 
'https://m.twitch.tv/thefranchiselive/about', 
'https://m.twitch.tv/losperifericosroyal/about', 
'https://m.twitch.tv/Scipionista/about', 
'https://m.twitch.tv/janusport/about', 
'https://m.twitch.tv/BridgetCase/about', 
'https://m.twitch.tv/RodrigoCapita/about', 
'https://m.twitch.tv/SalvatoRRR_OMG/about', 
'https://m.twitch.tv/tvaztecaesports/about', 
'https://m.twitch.tv/DonQuijoteDLC/about', 
'https://m.twitch.tv/fenixdeportestvv/about', 
'https://m.twitch.tv/chivasesports/about', 
'https://m.twitch.tv/lyesbouzidi/about', 
'https://m.twitch.tv/maajeestiic24/about', 
'https://m.twitch.tv/internetvbeisbol/about', 
'https://m.twitch.tv/TheDegenerateWeekly/about', 
'https://m.twitch.tv/rugbyramafr/about', 
'https://m.twitch.tv/CobraCards1/about', 
'https://m.twitch.tv/romainnextgen/about', 
'https://m.twitch.tv/barstoolgambling/about', 
'https://m.twitch.tv/baloncestoesp/about', 
'https://m.twitch.tv/JunkWaxVintage/about', 
'https://m.twitch.tv/ei_Franz/about', 
'https://m.twitch.tv/ArizonaDerbyDames/about', 
'https://m.twitch.tv/RoldanRodriguez/about', 
'https://m.twitch.tv/toptradingcardsde/about', 
'https://m.twitch.tv/EraUmBigMac_/about'

]

# Open a CSV file to write the results
with open('extracted_links.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Extracted Link'])  # Header row

    # Loop through each URL
    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all tags, which contain hyperlinks
        links = soup.find_all('a')
        # Extract the href attribute (URL) from each tag
        extracted_urls = [link.get('href') for link in links if link.get('href') and (link.get('href').startswith('http') or link.get('href').startswith('https'))]
        
        for extracted_url in extracted_urls:
            writer.writerow([url, extracted_url])  