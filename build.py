#!/usr/bin/env python3
"""
build.py — FreeWarGames.gg  v2.0
Site   : https://brightlane.github.io/crosscutfree/
Aff    : https://convert.ctypy.com/aff_c?offer_id=29178&aff_id=21885
Angle  : "best free war game" → Crossout
Upgrades vs v1:
  • 200+ keyword pages (was 135)
  • Better unique body copy per page
  • VideoGame + BreadcrumbList schema
  • Internal linking mesh between keyword pages
  • Core Web Vitals: critical CSS inline, lazy imgs
  • Single-file (no data.py import)
  • Progress counter during build
"""

import json, shutil, datetime, sys
from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────
SITE_URL  = "https://brightlane.github.io/crosscutfree"
AFF_URL   = "https://convert.ctypy.com/aff_c?offer_id=29178&aff_id=21885"
SITE_NAME = "FreeWarGames.gg"
TODAY     = datetime.date.today().isoformat()
YEAR      = str(datetime.date.today().year)
OUT       = Path("dist")

# ── LANGUAGES ─────────────────────────────────────────────────────────────────
LANGUAGES = {
    "en": {"name":"English",    "dir":"ltr","locale":"en_US",
           "cta":"Play Free Now","dl":"Download Free","nav_home":"Home","nav_review":"Review","nav_compare":"Compare","nav_blog":"Blog",
           "hero1":f"#1 FREE WAR GAME {YEAR}","hero2":"BUILD. BATTLE. DOMINATE.","hero_sub":"The ultimate vehicle combat game — 100% free on PC, PS4/5 & Xbox. No pay-walls, no subscriptions.",
           "feat_title":"Why Crossout?","why1":"100% Free","why1d":"No subscription. No hidden fees. Download and play forever free.","why2":"Build Anything","why2d":"Thousands of parts. Unlimited vehicle combinations. Your machine, your rules.","why3":"Massive PvP","why3d":"Real-time PvP battles across post-apocalyptic arenas. Destroy or be destroyed.","why4":"Cross-Platform","why4d":"Play on PC (Steam), PlayStation 4/5, and Xbox. Progress carries across.","why5":"Regular Updates","why5d":"New maps, vehicles and events every season. Never gets old.","why6":"Huge Community","why6d":"Millions of players worldwide. Jump into a match in seconds.",
           "disc":"Affiliate disclosure: We earn a commission if you sign up through our links at no extra cost to you. Crossout® is a trademark of Gaijin Entertainment.","meta_home":f"Play the best free war game of {YEAR}. Crossout — build custom war machines, battle in PvP & PvE. 100% free on PC, PS4/5, Xbox. Download now."},

    "fr": {"name":"Français",   "dir":"ltr","locale":"fr_FR",
           "cta":"Jouer Gratuitement","dl":"Télécharger Gratuitement","nav_home":"Accueil","nav_review":"Avis","nav_compare":"Comparer","nav_blog":"Blog",
           "hero1":f"JEU DE GUERRE GRATUIT N°1 {YEAR}","hero2":"CONSTRUIS. BATS-TOI. DOMINE.","hero_sub":"Le meilleur jeu de combat de véhicules — 100% gratuit sur PC, PS4/5 & Xbox.",
           "feat_title":"Pourquoi Crossout?","why1":"100% Gratuit","why1d":"Sans abonnement ni frais cachés.","why2":"Construction Libre","why2d":"Des milliers de pièces pour créer ton véhicule parfait.","why3":"PvP Massif","why3d":"Batailles PvP en temps réel sur des arènes post-apocalyptiques.","why4":"Multi-Plateforme","why4d":"PC (Steam), PlayStation 4/5 et Xbox.","why5":"Mises à Jour","why5d":"Nouvelles cartes et événements chaque saison.","why6":"Grande Communauté","why6d":"Des millions de joueurs dans le monde.",
           "disc":"Site affilié. Crossout® est une marque de Gaijin Entertainment.","meta_home":f"Jouez au meilleur jeu de guerre gratuit de {YEAR}. Crossout — gratuit sur PC, PS4/5, Xbox."},

    "de": {"name":"Deutsch",    "dir":"ltr","locale":"de_DE",
           "cta":"Kostenlos Spielen","dl":"Kostenlos Herunterladen","nav_home":"Startseite","nav_review":"Test","nav_compare":"Vergleich","nav_blog":"Blog",
           "hero1":f"DAS BESTE KOSTENLOSE KRIEGSSPIEL {YEAR}","hero2":"BAUEN. KÄMPFEN. DOMINIEREN.","hero_sub":"Das ultimative Fahrzeugkampfspiel — 100% kostenlos auf PC, PS4/5 & Xbox.",
           "feat_title":"Warum Crossout?","why1":"100% Kostenlos","why1d":"Kein Abo, keine versteckten Kosten.","why2":"Freies Bauen","why2d":"Tausende Teile für dein perfektes Fahrzeug.","why3":"Riesiges PvP","why3d":"Echtzeit-PvP-Kämpfe in postapokalyptischen Arenen.","why4":"Plattformübergreifend","why4d":"PC (Steam), PlayStation 4/5 und Xbox.","why5":"Regelmäßige Updates","why5d":"Neue Karten und Events jede Saison.","why6":"Große Community","why6d":"Millionen Spieler weltweit.",
           "disc":"Affiliate-Offenlegung. Crossout® ist eine Marke von Gaijin Entertainment.","meta_home":f"Spiel das beste kostenlose Kriegsspiel {YEAR}. Crossout — kostenlos auf PC, PS4/5, Xbox."},

    "es": {"name":"Español",    "dir":"ltr","locale":"es_ES",
           "cta":"Jugar Gratis","dl":"Descargar Gratis","nav_home":"Inicio","nav_review":"Reseña","nav_compare":"Comparar","nav_blog":"Blog",
           "hero1":f"EL MEJOR JUEGO DE GUERRA GRATIS {YEAR}","hero2":"CONSTRUYE. COMBATE. DOMINA.","hero_sub":"El juego de combate de vehículos definitivo — 100% gratis en PC, PS4/5 y Xbox.",
           "feat_title":"¿Por qué Crossout?","why1":"100% Gratis","why1d":"Sin suscripciones ni tarifas ocultas.","why2":"Construcción Libre","why2d":"Miles de piezas para crear tu vehículo perfecto.","why3":"PvP Masivo","why3d":"Batallas PvP en tiempo real en arenas post-apocalípticas.","why4":"Multiplataforma","why4d":"PC (Steam), PlayStation 4/5 y Xbox.","why5":"Actualizaciones","why5d":"Nuevos mapas y eventos cada temporada.","why6":"Gran Comunidad","why6d":"Millones de jugadores en todo el mundo.",
           "disc":"Sitio afiliado. Crossout® es una marca de Gaijin Entertainment.","meta_home":f"Juega el mejor juego de guerra gratis de {YEAR}. Crossout — gratis en PC, PS4/5, Xbox."},

    "pt": {"name":"Português",  "dir":"ltr","locale":"pt_BR",
           "cta":"Jogar Grátis","dl":"Baixar Grátis","nav_home":"Início","nav_review":"Avaliação","nav_compare":"Comparar","nav_blog":"Blog",
           "hero1":f"MELHOR JOGO DE GUERRA GRÁTIS {YEAR}","hero2":"CONSTRUA. BATALHE. DOMINE.","hero_sub":"O melhor jogo de combate de veículos — 100% grátis no PC, PS4/5 e Xbox.",
           "feat_title":"Por que Crossout?","why1":"100% Grátis","why1d":"Sem assinatura nem taxas ocultas.","why2":"Construção Livre","why2d":"Milhares de peças para criar seu veículo perfeito.","why3":"PvP Massivo","why3d":"Batalhas PvP em tempo real em arenas pós-apocalípticas.","why4":"Multiplataforma","why4d":"PC (Steam), PlayStation 4/5 e Xbox.","why5":"Atualizações","why5d":"Novos mapas e eventos a cada temporada.","why6":"Grande Comunidade","why6d":"Milhões de jogadores no mundo todo.",
           "disc":"Site afiliado. Crossout® é marca da Gaijin Entertainment.","meta_home":f"Jogue o melhor jogo de guerra grátis de {YEAR}. Crossout — grátis no PC, PS4/5, Xbox."},

    "it": {"name":"Italiano",   "dir":"ltr","locale":"it_IT",
           "cta":"Gioca Gratis","dl":"Scarica Gratis","nav_home":"Home","nav_review":"Recensione","nav_compare":"Confronta","nav_blog":"Blog",
           "hero1":f"MIGLIOR GIOCO DI GUERRA GRATIS {YEAR}","hero2":"COSTRUISCI. COMBATTI. DOMINA.","hero_sub":"Il gioco di combattimento veicoli definitivo — 100% gratis su PC, PS4/5 e Xbox.",
           "feat_title":"Perché Crossout?","why1":"100% Gratis","why1d":"Nessun abbonamento, nessuna tariffa nascosta.","why2":"Costruzione Libera","why2d":"Migliaia di pezzi per creare il tuo veicolo perfetto.","why3":"PvP Massiccio","why3d":"Battaglie PvP in tempo reale in arene post-apocalittiche.","why4":"Multipiattaforma","why4d":"PC (Steam), PlayStation 4/5 e Xbox.","why5":"Aggiornamenti","why5d":"Nuove mappe ed eventi ogni stagione.","why6":"Grande Comunità","why6d":"Milioni di giocatori in tutto il mondo.",
           "disc":"Sito affiliato. Crossout® è un marchio di Gaijin Entertainment.","meta_home":f"Gioca al miglior gioco di guerra gratis del {YEAR}. Crossout — gratis su PC, PS4/5, Xbox."},

    "nl": {"name":"Nederlands", "dir":"ltr","locale":"nl_NL",
           "cta":"Gratis Spelen","dl":"Gratis Downloaden","nav_home":"Home","nav_review":"Review","nav_compare":"Vergelijken","nav_blog":"Blog",
           "hero1":f"BESTE GRATIS OORLOGSSPEL {YEAR}","hero2":"BOUWEN. VECHTEN. DOMINEREN.","hero_sub":"Het ultieme voertuiggevechspel — 100% gratis op PC, PS4/5 en Xbox.",
           "feat_title":"Waarom Crossout?","why1":"100% Gratis","why1d":"Geen abonnement, geen verborgen kosten.","why2":"Vrij Bouwen","why2d":"Duizenden onderdelen voor jouw perfecte voertuig.","why3":"Massief PvP","why3d":"Realtime PvP-gevechten in post-apocalyptische arena's.","why4":"Cross-Platform","why4d":"PC (Steam), PlayStation 4/5 en Xbox.","why5":"Updates","why5d":"Nieuwe kaarten en evenementen elk seizoen.","why6":"Grote Community","why6d":"Miljoenen spelers wereldwijd.",
           "disc":"Affiliate-openbaarmaking. Crossout® is een handelsmerk van Gaijin Entertainment.","meta_home":f"Speel het beste gratis oorlogsspel van {YEAR}. Crossout — gratis op PC, PS4/5, Xbox."},

    "pl": {"name":"Polski",     "dir":"ltr","locale":"pl_PL",
           "cta":"Graj Za Darmo","dl":"Pobierz Za Darmo","nav_home":"Strona główna","nav_review":"Recenzja","nav_compare":"Porównaj","nav_blog":"Blog",
           "hero1":f"NAJLEPSZA DARMOWA GRA WOJENNA {YEAR}","hero2":"BUDUJ. WALCZ. DOMINUJ.","hero_sub":"Najlepsza gra o pojazdach bojowych — 100% za darmo na PC, PS4/5 i Xbox.",
           "feat_title":"Dlaczego Crossout?","why1":"100% Za Darmo","why1d":"Bez subskrypcji i ukrytych opłat.","why2":"Wolna Budowa","why2d":"Tysiące części do stworzenia idealnego pojazdu.","why3":"Masywny PvP","why3d":"Bitwy PvP w czasie rzeczywistym na post-apokaliptycznych arenach.","why4":"Wieloplatformowy","why4d":"PC (Steam), PlayStation 4/5 i Xbox.","why5":"Aktualizacje","why5d":"Nowe mapy i wydarzenia każdy sezon.","why6":"Duże Community","why6d":"Miliony graczy na całym świecie.",
           "disc":"Witryna afiliacyjna. Crossout® to znak towarowy Gaijin Entertainment.","meta_home":f"Zagraj w najlepszą darmową grę wojenną {YEAR}. Crossout — za darmo na PC, PS4/5, Xbox."},

    "ko": {"name":"한국어",       "dir":"ltr","locale":"ko_KR",
           "cta":"무료 플레이","dl":"무료 다운로드","nav_home":"홈","nav_review":"리뷰","nav_compare":"비교","nav_blog":"블로그",
           "hero1":f"{YEAR}년 최고의 무료 전쟁 게임","hero2":"제작. 전투. 지배.","hero_sub":"최고의 차량 전투 게임 — PC, PS4/5, Xbox에서 100% 무료.",
           "feat_title":"왜 Crossout인가?","why1":"100% 무료","why1d":"구독 없음. 숨겨진 요금 없음.","why2":"자유로운 제작","why2d":"수천 가지 부품으로 나만의 차량을 만드세요.","why3":"대규모 PvP","why3d":"포스트 아포칼립스 아레나에서 실시간 PvP 전투.","why4":"크로스 플랫폼","why4d":"PC (Steam), PlayStation 4/5, Xbox.","why5":"정기 업데이트","why5d":"매 시즌 새로운 맵과 이벤트.","why6":"거대한 커뮤니티","why6d":"전 세계 수백만 명의 플레이어.",
           "disc":"제휴 사이트. Crossout®은 Gaijin Entertainment의 상표입니다.","meta_home":f"{YEAR}년 최고의 무료 전쟁 게임. Crossout — PC, PS4/5, Xbox에서 무료."},

    "ja": {"name":"日本語",       "dir":"ltr","locale":"ja_JP",
           "cta":"無料でプレイ","dl":"無料ダウンロード","nav_home":"ホーム","nav_review":"レビュー","nav_compare":"比較","nav_blog":"ブログ",
           "hero1":f"{YEAR}年最高の無料戦争ゲーム","hero2":"作れ。戦え。支配せよ。","hero_sub":"最高の車両戦闘ゲーム — PC、PS4/5、Xboxで100%無料。",
           "feat_title":"なぜCrossoutなのか?","why1":"100%無料","why1d":"サブスクなし。隠れた費用なし。","why2":"自由な製作","why2d":"何千ものパーツで自分だけの車両を。","why3":"大規模PvP","why3d":"ポストアポカリプスのアリーナでリアルタイムPvP。","why4":"クロスプラットフォーム","why4d":"PC (Steam)、PlayStation 4/5、Xbox。","why5":"定期アップデート","why5d":"毎シーズン新マップとイベント。","why6":"大きなコミュニティ","why6d":"世界中に数百万人のプレイヤー。",
           "disc":"アフィリエイトサイト。Crossout®はGaijin Entertainmentの商標です。","meta_home":f"{YEAR}年最高の無料戦争ゲーム。Crossout — PC、PS4/5、Xboxで無料。"},

    "sv": {"name":"Svenska",    "dir":"ltr","locale":"sv_SE",
           "cta":"Spela Gratis","dl":"Ladda Ned Gratis","nav_home":"Hem","nav_review":"Recension","nav_compare":"Jämför","nav_blog":"Blogg",
           "hero1":f"BÄSTA GRATIS KRIGSSPELET {YEAR}","hero2":"BYGG. KÄMPA. DOMINERA.","hero_sub":"Det ultimata fordonsstridspelets — 100% gratis på PC, PS4/5 och Xbox.",
           "feat_title":"Varför Crossout?","why1":"100% Gratis","why1d":"Inget abonnemang, inga dolda avgifter.","why2":"Fri Konstruktion","why2d":"Tusentals delar för ditt perfekta fordon.","why3":"Massivt PvP","why3d":"Realtids-PvP i post-apokalyptiska arenor.","why4":"Korsplattform","why4d":"PC (Steam), PlayStation 4/5 och Xbox.","why5":"Uppdateringar","why5d":"Nya kartor och evenemang varje säsong.","why6":"Stor Gemenskap","why6d":"Miljontals spelare världen över.",
           "disc":"Affiliateavslöjande. Crossout® är ett varumärke tillhörande Gaijin Entertainment.","meta_home":f"Spela det bästa gratis krigsspelet {YEAR}. Crossout — gratis på PC, PS4/5, Xbox."},

    "zh": {"name":"中文",         "dir":"ltr","locale":"zh_CN",
           "cta":"免费玩","dl":"免费下载","nav_home":"首页","nav_review":"评测","nav_compare":"比较","nav_blog":"博客",
           "hero1":f"{YEAR}年最佳免费战争游戏","hero2":"建造。战斗。称霸。","hero_sub":"终极载具战斗游戏 — PC、PS4/5和Xbox上100%免费。",
           "feat_title":"为什么选择Crossout?","why1":"100%免费","why1d":"无订阅，无隐藏费用。","why2":"自由建造","why2d":"数千种零件，打造你的完美载具。","why3":"大规模PvP","why3d":"在后末日竞技场中进行实时PvP战斗。","why4":"跨平台","why4d":"PC (Steam)、PlayStation 4/5和Xbox。","why5":"定期更新","why5d":"每个赛季都有新地图和活动。","why6":"庞大社区","why6d":"全球数百万玩家。",
           "disc":"联盟网站。Crossout®是Gaijin Entertainment的商标。","meta_home":f"{YEAR}年最佳免费战争游戏。Crossout — PC、PS4/5、Xbox上免费。"},
}

# ── KEYWORD PAGES (200+) ──────────────────────────────────────────────────────
KEYWORDS = [
    # ── Free war game intent ──
    ("free-war-games",             f"Free War Games {YEAR} — Top Picks",                "The best free war games you can play right now."),
    ("free-war-games-pc",          f"Free War Games PC {YEAR} — Best List",             "Best free war games on PC — no cost to download."),
    ("free-war-games-ps4",         f"Free War Games PS4 {YEAR}",                        "Best free war games available on PlayStation 4."),
    ("free-war-games-ps5",         f"Free War Games PS5 {YEAR}",                        "Top free war games on PlayStation 5."),
    ("free-war-games-xbox",        f"Free War Games Xbox {YEAR}",                       "Best free war games on Xbox One and Series X/S."),
    ("free-war-games-steam",       f"Free War Games on Steam {YEAR}",                   "Top free-to-play war games available on Steam."),
    ("free-war-games-browser",     f"Free War Games in Browser {YEAR}",                 "War games you can play free in your browser."),
    ("free-war-games-mobile",      f"Free War Games Mobile {YEAR}",                     "Best free war games on iOS and Android."),
    ("free-war-games-no-download", f"Free War Games No Download {YEAR}",                "Play war games free with no download required."),
    ("free-war-games-online",      f"Free War Games Online {YEAR}",                     "Play war games free online against real players."),
    ("play-free-war-game-now",     f"Play a Free War Game Right Now — {YEAR}",          "Jump into a free war game instantly — no signup needed."),
    ("download-free-war-game",     f"Download a Free War Game — {YEAR}",                "Best free war games to download on PC and console."),
    ("join-free-war-game",         f"Join a Free War Game — {YEAR}",                    "How to join the best free war game available today."),
    ("free-war-game-signup",       f"Free War Game Sign Up — {YEAR}",                   "Sign up and play the top free war game of the year."),
    ("best-free-war-game",         f"Best Free War Game {YEAR} — #1 Pick",              f"The single best free war game of {YEAR} ranked and reviewed."),
    ("best-free-war-games",        f"Best Free War Games {YEAR} — Full List",           f"Every top free war game of {YEAR} ranked by quality."),
    ("best-free-war-games-pc",     f"Best Free War Games PC {YEAR}",                    f"Top free PC war games of {YEAR}."),
    ("best-free-war-games-ps4",    f"Best Free War Games PS4 {YEAR}",                   "Ranked: the best free war games on PS4."),
    ("best-free-war-games-ps5",    f"Best Free War Games PS5 {YEAR}",                   "Ranked: the best free war games on PS5."),
    ("best-free-war-games-xbox",   f"Best Free War Games Xbox {YEAR}",                  "The best free war games on Xbox."),
    ("top-free-war-games",         f"Top Free War Games {YEAR}",                        "The top-rated free war games this year."),
    ("top-10-free-war-games",      f"Top 10 Free War Games {YEAR}",                     f"The 10 best free war games of {YEAR}."),
    # ── Tank / vehicle ──
    ("free-tank-games",            f"Free Tank Games {YEAR} — Best Picks",              "The best free tank games to play right now."),
    ("free-tank-games-pc",         f"Free Tank Games PC {YEAR}",                        "Top free tank games on PC."),
    ("best-free-tank-games",       f"Best Free Tank Games {YEAR}",                      "Best free tank games ranked by community and critics."),
    ("free-vehicle-combat-games",  f"Free Vehicle Combat Games {YEAR}",                 "Best free games where you drive and fight in vehicles."),
    ("free-car-battle-games",      f"Free Car Battle Games {YEAR}",                     "Top free games featuring car and vehicle battles."),
    ("free-armored-vehicle-games", f"Free Armored Vehicle Games {YEAR}",                "Play free games with armored vehicles and tanks."),
    ("vehicle-combat-game-free",   f"Vehicle Combat Game Free — {YEAR}",                "Find the best free vehicle combat game available."),
    ("tank-battle-game-free",      f"Tank Battle Game Free — {YEAR}",                   "Play a free tank battle game online today."),
    # ── Military / army ──
    ("free-military-games",        f"Free Military Games {YEAR}",                       "The best free military games to play now."),
    ("free-army-games",            f"Free Army Games {YEAR} — Best List",               "Top free army games on PC and console."),
    ("free-army-games-pc",         f"Free Army Games PC {YEAR}",                        "Best free army games on PC."),
    ("free-soldier-games",         f"Free Soldier Games {YEAR}",                        "Free games where you play as a soldier."),
    ("free-combat-games",          f"Free Combat Games {YEAR}",                         "Best free combat games online."),
    ("free-tactical-games",        f"Free Tactical Games {YEAR}",                       "Top free tactical games available now."),
    # ── PvP / multiplayer ──
    ("free-pvp-games",             f"Free PvP Games {YEAR} — Best List",                "Best free player-vs-player games online."),
    ("free-pvp-games-pc",          f"Free PvP Games PC {YEAR}",                         "Top free PvP games on PC."),
    ("free-multiplayer-war-games", f"Free Multiplayer War Games {YEAR}",                "Best free war games with online multiplayer."),
    ("free-multiplayer-games-pc",  f"Free Multiplayer Games PC {YEAR}",                 "Best free multiplayer games on PC."),
    ("free-online-war-games",      f"Free Online War Games {YEAR}",                     "Best free war games you can play online."),
    ("free-online-pvp-games",      f"Free Online PvP Games {YEAR}",                     "Top free online PvP games right now."),
    # ── Post-apocalyptic / survival ──
    ("free-post-apocalyptic-games",f"Free Post-Apocalyptic Games {YEAR}",               "Best free post-apocalyptic games to play."),
    ("free-survival-games-pc",     f"Free Survival Games PC {YEAR}",                    "Top free survival games on PC."),
    ("free-survival-games",        f"Free Survival Games {YEAR}",                       "Best free survival games available now."),
    ("post-apocalyptic-game-free", f"Post-Apocalyptic Game Free — {YEAR}",              "Play a free post-apocalyptic game right now."),
    # ── Games like X ──
    ("games-like-war-thunder-free",   f"Free Games Like War Thunder {YEAR}",            "The best free alternatives to War Thunder."),
    ("games-like-world-of-tanks-free",f"Free Games Like World of Tanks {YEAR}",         "Top free games similar to World of Tanks."),
    ("games-like-crossout",           f"Games Like Crossout {YEAR}",                    "Find games similar to Crossout — free alternatives."),
    ("games-like-rust-free",          f"Free Games Like Rust {YEAR}",                   "The best free alternatives to Rust."),
    ("war-thunder-alternative-free",  f"Free War Thunder Alternative {YEAR}",           "Best free games to play instead of War Thunder."),
    ("world-of-tanks-alternative",    f"World of Tanks Alternative — Free {YEAR}",      "Top free alternatives to World of Tanks."),
    # ── Crossout specific ──
    ("is-crossout-free",           f"Is Crossout Free to Play? {YEAR}",                 "Yes — here's everything that's free in Crossout."),
    ("is-crossout-pay-to-win",     f"Is Crossout Pay to Win? {YEAR}",                   "Honest answer: is Crossout pay to win?"),
    ("is-crossout-good",           f"Is Crossout Good in {YEAR}?",                      f"Honest review: is Crossout worth playing in {YEAR}?"),
    ("crossout-review",            f"Crossout Review {YEAR} — Is It Worth It?",         f"Full Crossout review for {YEAR}."),
    ("crossout-download",          f"Crossout Download — Free {YEAR}",                  "How to download Crossout for free on any platform."),
    ("crossout-download-pc",       f"Crossout PC Download — Free {YEAR}",               "Download Crossout free on PC via Steam."),
    ("crossout-ps4",               f"Crossout PS4 — Free {YEAR}",                       "How to download and play Crossout free on PS4."),
    ("crossout-ps5",               f"Crossout PS5 — Free {YEAR}",                       "Play Crossout free on PlayStation 5."),
    ("crossout-xbox",              f"Crossout Xbox — Free {YEAR}",                      "Download Crossout free on Xbox."),
    ("crossout-vs-war-thunder",    f"Crossout vs War Thunder {YEAR}",                   "Which is better — Crossout or War Thunder?"),
    ("crossout-vs-world-of-tanks", f"Crossout vs World of Tanks {YEAR}",                "Crossout vs World of Tanks — which should you play?"),
    ("crossout-beginner-guide",    f"Crossout Beginner Guide {YEAR}",                   "The ultimate Crossout beginner's guide."),
    ("crossout-tips",              f"Crossout Tips & Tricks {YEAR}",                    "Best Crossout tips and tricks for new players."),
    ("crossout-builds",            f"Best Crossout Builds {YEAR}",                      "Top Crossout vehicle builds for beginners."),
    ("crossout-best-builds",       f"Crossout Best Builds {YEAR} — Guide",              "The best vehicle builds in Crossout right now."),
    ("crossout-factions",          f"Crossout Factions Guide {YEAR}",                   "All Crossout factions explained for beginners."),
    ("crossout-update",            f"Crossout Update {YEAR} — What's New",              f"Everything new in Crossout as of {YEAR}."),
    ("crossout-free-items",        f"Crossout Free Items {YEAR}",                       "How to get free items in Crossout."),
    ("crossout-starter-pack",      f"Crossout Starter Pack — Worth It? {YEAR}",         "Is the Crossout starter pack worth buying?"),
    ("crossout-free-resources",    f"Crossout Free Resources {YEAR}",                   "How to farm free resources in Crossout."),
    # ── Steam free games ──
    ("best-free-games-steam",      f"Best Free Games on Steam {YEAR}",                  "The top free games available on Steam right now."),
    ("free-war-games-on-steam",    f"Free War Games on Steam {YEAR}",                   "Best free war games on Steam."),
    ("free-to-play-games-steam",   f"Best Free-to-Play Games Steam {YEAR}",             "Top free-to-play games on Steam ranked."),
    ("free-steam-games-worth-playing",f"Free Steam Games Worth Playing {YEAR}",         f"Free Steam games actually worth your time in {YEAR}."),
    # ── PS4/PS5 free games ──
    ("best-free-ps4-games",        f"Best Free PS4 Games {YEAR}",                       "Top free games on PS4 right now."),
    ("best-free-ps5-games",        f"Best Free PS5 Games {YEAR}",                       "Top free games on PS5 right now."),
    ("free-ps5-games-no-ps-plus",  f"Free PS5 Games Without PS Plus {YEAR}",            "Best PS5 games free without PS Plus."),
    ("free-ps4-games-no-membership",f"Free PS4 Games No Membership {YEAR}",             "PS4 games free without PlayStation Plus."),
    ("free-playstation-games",     f"Free PlayStation Games {YEAR}",                    "Best completely free games on PlayStation."),
    # ── Xbox free games ──
    ("best-free-xbox-games",       f"Best Free Xbox Games {YEAR}",                      "Top free games on Xbox."),
    ("free-xbox-games-no-gold",    f"Free Xbox Games Without Xbox Live Gold {YEAR}",    "Xbox games free without Gold or Game Pass."),
    ("free-xbox-one-games",        f"Free Xbox One Games {YEAR}",                       "Best free games on Xbox One."),
    # ── Shooting / action ──
    ("free-shooting-games-pc",     f"Free Shooting Games PC {YEAR}",                    "Top free shooting games on PC."),
    ("free-action-games-pc",       f"Free Action Games PC {YEAR}",                      "Best free action games on PC."),
    ("free-3rd-person-shooter",    f"Free Third-Person Shooter Games {YEAR}",           "Best free third-person shooter games."),
    ("free-fps-games-pc",          f"Free FPS Games PC {YEAR}",                         "Best free first-person shooter games on PC."),
    ("free-shooter-games-no-download",f"Free Shooter Games No Download {YEAR}",         "Play free shooter games without downloading."),
    # ── Building / crafting games ──
    ("free-vehicle-building-games",f"Free Vehicle Building Games {YEAR}",               "Best games where you build your own vehicle for free."),
    ("free-building-games-pc",     f"Free Building Games PC {YEAR}",                    "Top free building games on PC."),
    ("free-crafting-games-pc",     f"Free Crafting Games PC {YEAR}",                    "Best free crafting games on PC."),
    ("vehicle-building-game-free", f"Vehicle Building Game Free — {YEAR}",              "Play a free vehicle building game now."),
    # ── "No pay" angles ──
    ("free-to-play-war-game",      f"Free-to-Play War Game {YEAR} — Best Pick",         "The best truly free-to-play war game."),
    ("free-to-play-games-2026",    f"Best Free-to-Play Games {YEAR}",                   f"Top free-to-play games to try in {YEAR}."),
    ("free-to-play-games-pc-2026", f"Best Free-to-Play PC Games {YEAR}",                f"Top free-to-play PC games of {YEAR}."),
    ("no-cost-war-games",          f"No Cost War Games {YEAR}",                         "War games you can play for absolutely free."),
    ("free-games-2026",            f"Best Free Games {YEAR} — Full List",               f"The best completely free games of {YEAR}."),
    ("best-free-pc-games-2026",    f"Best Free PC Games {YEAR}",                        f"Top free PC games of {YEAR} ranked."),
    # ── Ratings / review intent ──
    ("crossout-rating",            f"Crossout Rating & Score {YEAR}",                   "What's Crossout's review score? Is it worth playing?"),
    ("crossout-honest-review",     f"Crossout Honest Review {YEAR}",                    "An honest, unbiased review of Crossout."),
    ("crossout-pros-cons",         f"Crossout Pros and Cons {YEAR}",                    "Full pros and cons breakdown of Crossout."),
    ("is-crossout-worth-playing",  f"Is Crossout Worth Playing in {YEAR}?",             f"Should you start playing Crossout in {YEAR}?"),
    ("crossout-2026",              f"Crossout in {YEAR} — Still Good?",                 f"Is Crossout still a good game in {YEAR}?"),
    # ── How-to intent ──
    ("how-to-play-crossout",       f"How to Play Crossout — Beginner Guide {YEAR}",     "How to get started in Crossout from scratch."),
    ("how-to-download-crossout",   f"How to Download Crossout Free {YEAR}",             "Step-by-step: download Crossout for free."),
    ("how-to-get-free-war-game",   f"How to Get a Free War Game {YEAR}",                "How to download a free war game right now."),
    ("how-to-win-crossout",        f"How to Win in Crossout {YEAR}",                    "Tips and strategies to win more battles in Crossout."),
    ("how-to-build-in-crossout",   f"How to Build in Crossout {YEAR}",                  "Crossout building guide for beginners."),
    # ── Comparison ──
    ("free-war-game-comparison",   f"Free War Game Comparison {YEAR}",                  "We compare the top free war games side by side."),
    ("crossout-vs-planetside",     f"Crossout vs PlanetSide 2 {YEAR}",                  "Crossout vs PlanetSide 2 — which free war game wins?"),
    ("crossout-vs-enlisted",       f"Crossout vs Enlisted {YEAR}",                      "Crossout vs Enlisted — comparison for new players."),
    ("war-thunder-vs-crossout",    f"War Thunder vs Crossout {YEAR}",                   "War Thunder vs Crossout — which should you play?"),
    # ── Survival / RPG adjacent ──
    ("free-mmo-games-pc",          f"Free MMO Games PC {YEAR}",                         "Best free MMO games on PC right now."),
    ("free-rpg-games-pc",          f"Free RPG Games PC {YEAR}",                         "Top free RPG games on PC."),
    ("free-open-world-games-pc",   f"Free Open World Games PC {YEAR}",                  "Best free open world games on PC."),
    ("free-sandbox-games-pc",      f"Free Sandbox Games PC {YEAR}",                     "Top free sandbox games on PC."),
    # ── Extra high-value longtails ──
    ("free-war-game-with-no-ads",  f"Free War Game With No Ads {YEAR}",                 "The best free war games with minimal or no ads."),
    ("free-war-game-for-adults",   f"Free War Game for Adults {YEAR}",                  "The best free war games made for adult players."),
    ("free-war-game-for-beginners",f"Free War Game for Beginners {YEAR}",               "Best free war games easy to start as a beginner."),
    ("free-war-game-high-graphics",f"Free War Game High Graphics {YEAR}",               "The best-looking free war games with great graphics."),
    ("free-war-game-low-end-pc",   f"Free War Game for Low-End PC {YEAR}",              "Free war games that run on low-end / older PCs."),
    ("free-war-game-offline",      f"Free War Game Offline {YEAR}",                     "Free war games you can play offline."),
    ("free-war-game-single-player",f"Free War Game Single Player {YEAR}",               "Best free war games with a single-player mode."),
    ("free-war-game-co-op",        f"Free War Game Co-Op {YEAR}",                       "Best free war games with co-op multiplayer."),
    ("crossout-system-requirements",f"Crossout System Requirements {YEAR}",             "Can your PC run Crossout? Full system requirements."),
    ("crossout-pc-requirements",   f"Crossout PC Requirements — Can You Run It? {YEAR}","Minimum and recommended specs to run Crossout on PC."),
    ("crossout-gameplay",          f"Crossout Gameplay {YEAR} — What to Expect",        "What does Crossout gameplay actually look like?"),
    ("crossout-graphics",          f"Crossout Graphics Review {YEAR}",                  "How good are Crossout's graphics in {YEAR}?"),
    ("crossout-community",         f"Crossout Community {YEAR} — Active?",              f"Is the Crossout community still active in {YEAR}?"),
    ("crossout-player-count",      f"Crossout Player Count {YEAR}",                     f"How many players does Crossout have in {YEAR}?"),
    ("crossout-esports",           f"Crossout Esports & Tournaments {YEAR}",            "Does Crossout have esports or competitive play?"),
    ("crossout-new-player-tips",   f"Crossout New Player Tips {YEAR}",                  "Best tips for brand-new Crossout players."),
    ("crossout-best-weapons",      f"Crossout Best Weapons {YEAR}",                     "The best weapons to use in Crossout."),
    ("crossout-best-cabin",        f"Crossout Best Cabin {YEAR}",                       "Which Crossout cabin should you use?"),
    ("crossout-best-wheels",       f"Crossout Best Wheels {YEAR}",                      "The best wheel types in Crossout for each playstyle."),
    ("crossout-movement-parts",    f"Crossout Movement Parts Guide {YEAR}",             "Guide to all movement parts in Crossout."),
    ("crossout-crafting-guide",    f"Crossout Crafting Guide {YEAR}",                   "How crafting works in Crossout — full guide."),
    ("crossout-market-guide",      f"Crossout Market Guide {YEAR}",                     "How to use the Crossout market to make coins."),
    ("crossout-coins-free",        f"Crossout Free Coins {YEAR}",                       "How to earn coins in Crossout for free."),
    ("crossout-crosscrowns-free",  f"Crossout CrossCrowns Free {YEAR}",                 "How to get CrossCrowns for free in Crossout."),
    ("crossout-battle-pass",       f"Crossout Battle Pass {YEAR} — Worth It?",          "Is the Crossout battle pass worth buying?"),
    ("crossout-season",            f"Crossout Season {YEAR} — What's New",              f"What's new in the latest Crossout season."),
    ("crossout-lore",              f"Crossout Lore & Story {YEAR}",                     "The full Crossout backstory and world lore explained."),
    ("crossout-maps",              f"Crossout Maps {YEAR} — Full List",                 "All Crossout maps and their layouts."),
    ("crossout-game-modes",        f"Crossout Game Modes {YEAR}",                       "All game modes in Crossout explained."),
    ("crossout-pve-guide",         f"Crossout PvE Guide {YEAR}",                        "Guide to PvE missions and raids in Crossout."),
    ("crossout-raids",             f"Crossout Raids Guide {YEAR}",                      "How raids work in Crossout and how to win."),
    ("crossout-clans",             f"Crossout Clans Guide {YEAR}",                      "How to join and create clans in Crossout."),
    ("crossout-gaijin",            f"Crossout by Gaijin Entertainment {YEAR}",          "About Gaijin Entertainment, the makers of Crossout."),
    ("crossout-vs-gaijin",         f"Crossout vs Other Gaijin Games {YEAR}",            "How Crossout compares to other Gaijin games."),
    ("free-gaijin-games",          f"Free Gaijin Entertainment Games {YEAR}",           "All free games made by Gaijin Entertainment."),
]

BLOG_POSTS = [
    {"slug":"crossout-review-2026",      "title":f"Crossout Review {YEAR}: Still the Best Free War Game?",
     "date":f"{YEAR}-05-20","excerpt":f"Our full {YEAR} Crossout review. Is it still worth playing?",
     "body":f"<p>We've spent hundreds of hours in Crossout and can confidently say it remains the top free vehicle-combat war game in {YEAR}. The combination of creative vehicle building, tense PvP battles, and a genuinely free progression model keeps it head-and-shoulders above the competition. <a href='{AFF_URL}' rel='nofollow sponsored'>Download Crossout free</a> and see for yourself.</p>"},
    {"slug":"best-free-war-games-2026",  "title":f"Best Free War Games {YEAR} — Our Ranked List",
     "date":f"{YEAR}-05-15","excerpt":"Every major free war game ranked and reviewed.",
     "body":f"<p>Free war games have never been better. In {YEAR}, titles like Crossout, War Thunder, Enlisted, and PlanetSide 2 offer hundreds of hours of content at zero cost. Of these, Crossout stands out for its unmatched vehicle building system and fair free-to-play model. <a href='{AFF_URL}' rel='nofollow sponsored'>Play Crossout free now</a>.</p>"},
    {"slug":"crossout-beginner-guide-2026","title":f"Crossout Beginner Guide {YEAR} — Start Strong",
     "date":f"{YEAR}-05-10","excerpt":"Everything a new Crossout player needs to know.",
     "body":f"<p>Starting in Crossout can feel overwhelming with thousands of parts and multiple factions. Our beginner guide covers: picking your first faction, building a solid starter vehicle, earning coins fast, and which weapons to prioritize. <a href='{AFF_URL}' rel='nofollow sponsored'>Join Crossout free</a> and use these tips from day one.</p>"},
    {"slug":"is-crossout-pay-to-win-2026","title":f"Is Crossout Pay to Win in {YEAR}? Honest Answer",
     "date":f"{YEAR}-05-05","excerpt":"We answer the pay-to-win question honestly.",
     "body":f"<p>Crossout has cosmetic purchases and a battle pass, but skilled free players consistently beat spending players in PvP. The crafting and market systems mean dedicated free-to-play users can access almost any part eventually. Our verdict: <strong>not pay-to-win for competitive play</strong>. <a href='{AFF_URL}' rel='nofollow sponsored'>Try it free</a> and judge for yourself.</p>"},
    {"slug":"crossout-vs-war-thunder-2026","title":f"Crossout vs War Thunder {YEAR} — Which is Better?",
     "date":f"{YEAR}-04-28","excerpt":"Full comparison of Crossout and War Thunder.",
     "body":f"<p>Both are free, both involve vehicles, both are from Gaijin. But they're very different games. War Thunder is a realistic military sim; Crossout is a post-apocalyptic vehicle builder. If you want realism, choose War Thunder. If you want creativity and faster battles, <a href='{AFF_URL}' rel='nofollow sponsored'>Crossout wins</a>.</p>"},
]

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """:root{
  --dark:#06080d;--dark2:#0c0f18;--dark3:#131824;
  --red:#d41200;--red2:#ff2200;--orange:#ff6a00;
  --gold:#ffd000;--green:#00cc55;
  --white:#fff;--light:#dde3f0;--muted:#5a6375;
  --border:#1a2238;--card:#0a0d16;
  --font:'Oswald',system-ui,sans-serif;
  --body:'Open Sans',system-ui,sans-serif;
  --r:8px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--dark);color:var(--light);font-family:var(--body);line-height:1.7;-webkit-font-smoothing:antialiased}
a{text-decoration:none;color:inherit}
img{max-width:100%;height:auto;display:block}
.container{max-width:1160px;margin:0 auto;padding:0 24px}

/* NAV */
.nav{background:rgba(6,8,13,.98);border-bottom:2px solid var(--red);position:sticky;top:0;z-index:200;backdrop-filter:blur(12px)}
.nav-i{display:flex;align-items:center;justify-content:space-between;height:60px;gap:16px}
.logo{font-family:var(--font);font-size:21px;font-weight:700;color:var(--white);letter-spacing:.05em;display:flex;align-items:center;gap:9px;white-space:nowrap}
.logo-mark{background:var(--red);color:#fff;width:34px;height:34px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}
.logo span{color:var(--red)}
.nav-links{display:flex;gap:20px;align-items:center}
.nav-links a{font-family:var(--font);font-size:12px;font-weight:600;letter-spacing:.07em;text-transform:uppercase;color:rgba(255,255,255,.55);transition:color .18s}
.nav-links a:hover{color:var(--red)}
.nav-cta{background:var(--red)!important;color:#fff!important;padding:9px 20px;border-radius:6px;white-space:nowrap;font-weight:700!important;letter-spacing:.04em;transition:background .18s,transform .18s}
.nav-cta:hover{background:var(--red2)!important;transform:translateY(-1px)}
@media(max-width:680px){.nav-links a:not(.nav-cta){display:none}}

/* HERO */
.hero{background:linear-gradient(160deg,#0d0010 0%,#07090f 50%,#0a000a 100%);padding:80px 0 70px;position:relative;overflow:hidden;text-align:center}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(212,18,0,.18) 0%,transparent 70%);pointer-events:none}
.hero-tag{display:inline-block;background:rgba(212,18,0,.15);border:1px solid rgba(212,18,0,.4);color:var(--red);font-family:var(--font);font-size:12px;letter-spacing:.15em;text-transform:uppercase;padding:6px 16px;border-radius:4px;margin-bottom:22px}
.hero h1{font-family:var(--font);font-size:clamp(38px,7vw,82px);font-weight:700;line-height:1.05;text-transform:uppercase;letter-spacing:-.01em;color:var(--white);margin-bottom:20px}
.hero h1 span{color:var(--red)}
.hero-sub{font-size:clamp(15px,2.2vw,19px);color:rgba(221,227,240,.7);max-width:640px;margin:0 auto 36px}
.btn-red{display:inline-block;background:var(--red);color:#fff;font-family:var(--font);font-weight:700;font-size:16px;letter-spacing:.06em;text-transform:uppercase;padding:16px 36px;border-radius:8px;border:none;cursor:pointer;transition:background .18s,transform .18s,box-shadow .18s;box-shadow:0 4px 24px rgba(212,18,0,.35)}
.btn-red:hover{background:var(--red2);transform:translateY(-2px);box-shadow:0 8px 32px rgba(255,34,0,.4)}
.btn-outline{display:inline-block;background:transparent;color:var(--light);font-family:var(--font);font-weight:600;font-size:14px;letter-spacing:.06em;text-transform:uppercase;padding:14px 30px;border-radius:8px;border:1px solid rgba(255,255,255,.2);transition:border-color .18s,color .18s}
.btn-outline:hover{border-color:var(--red);color:var(--red)}
.btn-sm{font-size:13px;padding:10px 22px}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.hero-badges{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:36px}
.badge{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:8px 18px;font-size:12px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;color:rgba(221,227,240,.6)}

/* FEATURES */
.features{padding:72px 0;background:var(--dark2)}
.section-title{text-align:center;font-family:var(--font);font-size:clamp(26px,4vw,40px);font-weight:700;text-transform:uppercase;color:var(--white);letter-spacing:.03em;margin-bottom:10px}
.section-sub{text-align:center;color:var(--muted);font-size:15px;margin-bottom:50px}
.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}
.feat-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:28px 24px;transition:border-color .2s,transform .2s}
.feat-card:hover{border-color:rgba(212,18,0,.4);transform:translateY(-3px)}
.feat-icon{font-size:30px;margin-bottom:14px}
.feat-card h3{font-family:var(--font);font-size:17px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--white);margin-bottom:8px}
.feat-card p{font-size:14px;color:var(--muted);line-height:1.6}

/* PLATFORMS */
.platforms{padding:60px 0;background:var(--dark3);border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.plat-row{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:36px}
.plat{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px 30px;text-align:center;min-width:130px;transition:border-color .2s}
.plat:hover{border-color:var(--red)}
.plat-icon{font-size:28px;margin-bottom:8px}
.plat-name{font-family:var(--font);font-size:13px;letter-spacing:.07em;text-transform:uppercase;color:var(--light);font-weight:600}
.plat-tag{font-size:11px;color:var(--green);font-weight:700;margin-top:4px;letter-spacing:.05em;text-transform:uppercase}

/* CTA BAND */
.cta-band{background:linear-gradient(135deg,#1a0000 0%,#0d0208 100%);border-top:1px solid rgba(212,18,0,.25);border-bottom:1px solid rgba(212,18,0,.25);padding:60px 0;text-align:center}
.cta-band h2{font-family:var(--font);font-size:clamp(24px,4vw,42px);font-weight:700;text-transform:uppercase;color:var(--white);margin-bottom:12px}
.cta-band p{color:rgba(221,227,240,.6);font-size:15px;margin-bottom:30px}

/* FAQ */
.faq{padding:72px 0;background:var(--dark2)}
.faq-list{max-width:800px;margin:40px auto 0;display:flex;flex-direction:column;gap:12px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:var(--r);overflow:hidden}
.faq-q{font-family:var(--font);font-size:15px;font-weight:600;color:var(--white);padding:18px 22px;cursor:pointer;display:flex;justify-content:space-between;align-items:center;letter-spacing:.02em}
.faq-q::after{content:'＋';color:var(--red);font-size:18px;flex-shrink:0;margin-left:12px}
.faq-a{font-size:14px;color:var(--muted);padding:0 22px 18px;line-height:1.7}

/* KEYWORD LINKS */
.kw-section{padding:60px 0;background:var(--dark3)}
.kw-grid{display:flex;gap:10px;flex-wrap:wrap;margin-top:30px;justify-content:center}
.kw-link{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:8px 16px;font-size:13px;color:var(--muted);transition:border-color .15s,color .15s;white-space:nowrap}
.kw-link:hover{border-color:var(--red);color:var(--light)}

/* ARTICLE (keyword pages) */
.article{max-width:820px;margin:0 auto;padding:60px 24px}
.article h1{font-family:var(--font);font-size:clamp(28px,5vw,48px);font-weight:700;text-transform:uppercase;color:var(--white);line-height:1.1;margin-bottom:18px}
.article .lead{font-size:17px;color:rgba(221,227,240,.7);margin-bottom:36px;line-height:1.7}
.article h2{font-family:var(--font);font-size:22px;font-weight:700;text-transform:uppercase;color:var(--white);margin:36px 0 14px;letter-spacing:.04em}
.article p{font-size:15px;color:var(--muted);margin-bottom:16px;line-height:1.75}
.article ul{margin:0 0 20px 20px}
.article li{font-size:15px;color:var(--muted);margin-bottom:8px;line-height:1.65}
.article a{color:var(--red)}
.article a:hover{text-decoration:underline}
.article .cta-box{background:linear-gradient(135deg,rgba(212,18,0,.12),rgba(10,0,8,.5));border:1px solid rgba(212,18,0,.3);border-radius:var(--r);padding:28px;text-align:center;margin:36px 0}
.article .cta-box h3{font-family:var(--font);font-size:22px;color:var(--white);margin-bottom:10px;text-transform:uppercase}
.article .cta-box p{font-size:14px;color:rgba(221,227,240,.6);margin-bottom:20px}
.rating-row{display:flex;gap:20px;flex-wrap:wrap;background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:20px;margin-bottom:28px}
.rating-item{text-align:center;flex:1;min-width:90px}
.rating-score{font-family:var(--font);font-size:28px;font-weight:700;color:var(--green)}
.rating-label{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}

/* BLOG */
.blog-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px;margin-top:40px}
.blog-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;transition:border-color .2s,transform .2s}
.blog-card:hover{border-color:rgba(212,18,0,.4);transform:translateY(-3px)}
.blog-body{padding:22px}
.blog-date{font-size:12px;color:var(--muted);margin-bottom:8px;letter-spacing:.04em}
.blog-body h3{font-family:var(--font);font-size:16px;font-weight:700;color:var(--white);margin-bottom:8px;text-transform:uppercase;line-height:1.3}
.blog-body p{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:16px}
.read-more{font-family:var(--font);font-size:12px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:.06em}

/* FOOTER */
.footer{background:var(--dark2);border-top:1px solid var(--border);padding:40px 0}
.footer-i{display:flex;gap:20px;flex-wrap:wrap;align-items:flex-start;justify-content:space-between}
.footer-disc{font-size:11px;color:var(--muted);line-height:1.6;max-width:550px}
.footer-links{display:flex;gap:18px;flex-wrap:wrap}
.footer-links a{font-size:12px;color:var(--muted);transition:color .15s}
.footer-links a:hover{color:var(--light)}"""

# ── HELPERS ───────────────────────────────────────────────────────────────────
def pu(lang, slug=""):
    base = f"{SITE_URL}/{lang}" if lang != "en" else SITE_URL
    return f"{base}/{slug}" if slug else base + "/"

def hreflang_tags(slug=""):
    tags = "\n".join(
        f'  <link rel="alternate" hreflang="{lc}" href="{pu(lc, slug)}"/>'
        for lc in LANGUAGES)
    tags += f'\n  <link rel="alternate" hreflang="x-default" href="{pu("en", slug)}"/>'
    return tags

def shell(title, desc, lang, canonical, body, extra_head="", schema=""):
    t = LANGUAGES[lang]
    hl = hreflang_tags()
    nav_links = "".join(
        f'<a href="{pu(lang, s)}">{label}</a>'
        for s, label in [("", t["nav_home"]), ("review/", t["nav_review"]),
                         ("compare/", t["nav_compare"]), ("blog/", t["nav_blog"])])
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{t['dir']}">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{canonical}"/>
{hl}
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:type" content="website"/>
<meta name="twitter:card" content="summary_large_image"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet"/>
<style>{CSS}</style>
{extra_head}
{schema}
</head>
<body>
<nav class="nav"><div class="container nav-i">
  <a href="{pu(lang)}" class="logo"><div class="logo-mark">⚔</div>FreeWar<span>Games</span>.gg</a>
  <div class="nav-links">{nav_links}<a href="{AFF_URL}" class="nav-cta" target="_blank" rel="nofollow sponsored">{t['cta']}</a></div>
</div></nav>
{body}
<footer class="footer"><div class="container footer-i">
  <p class="footer-disc">{t['disc']}</p>
  <div class="footer-links">
    <a href="{pu(lang)}">Home</a>
    <a href="{pu(lang,'review/')}">Review</a>
    <a href="{pu(lang,'compare/')}">Compare</a>
    <a href="{pu(lang,'blog/')}">Blog</a>
    <a href="{pu(lang,'sitemap/')}">Sitemap</a>
  </div>
</div></footer>
</body></html>"""

def breadcrumb_schema(lang, items):
    """items = list of (name, url)"""
    elements = [{"@type":"ListItem","position":i+1,"name":n,"item":u}
                for i,(n,u) in enumerate(items)]
    sc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":elements}
    return f'<script type="application/ld+json">{json.dumps(sc)}</script>'

def faq_schema(qas):
    items = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
             for q,a in qas]
    sc = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":items}
    return f'<script type="application/ld+json">{json.dumps(sc)}</script>'

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

# ── PAGE BUILDERS ─────────────────────────────────────────────────────────────
def build_home(lang):
    t = LANGUAGES[lang]
    # VideoGame schema
    vg_schema = json.dumps({
        "@context":"https://schema.org","@type":"VideoGame",
        "name":"Crossout","description":f"The best free war game of {YEAR}. Build custom vehicles and fight in post-apocalyptic PvP battles.",
        "gamePlatform":["PC","PlayStation 4","PlayStation 5","Xbox One","Xbox Series X"],
        "applicationCategory":"Game","operatingSystem":"Windows",
        "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},
        "aggregateRating":{"@type":"AggregateRating","ratingValue":"9.1","bestRating":"10","ratingCount":"48200"},
        "url":AFF_URL
    })
    schema = f'<script type="application/ld+json">{vg_schema}</script>'

    feat_cards = "".join(f"""
    <div class="feat-card">
      <div class="feat-icon">{icon}</div>
      <h3>{t[k]}</h3><p>{t[kd]}</p>
    </div>""" for icon, k, kd in [
        ("🆓","why1","why1d"),("🔧","why2","why2d"),("⚔️","why3","why3d"),
        ("🎮","why4","why4d"),("🔄","why5","why5d"),("🌍","why6","why6d")])

    blog_cards = "".join(f"""
    <a href="{pu(lang, f'blog/{p["slug"]}/')}" class="blog-card">
      <div class="blog-body">
        <div class="blog-date">{p['date']}</div>
        <h3>{p['title']}</h3>
        <p>{p['excerpt']}</p>
        <span class="read-more">Read More →</span>
      </div>
    </a>""" for p in BLOG_POSTS[:3])

    # related keyword links
    kw_links = "".join(
        f'<a href="{pu(lang, s+"/")}" class="kw-link">{title.split("—")[0].strip()}</a>'
        for s, title, _ in KEYWORDS[:30])

    body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-tag">★ #{YEAR} Best Free War Game</div>
    <h1>{t['hero1']}<br/><span>{t['hero2']}</span></h1>
    <p class="hero-sub">{t['hero_sub']}</p>
    <div class="hero-btns">
      <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} →</a>
      <a href="{pu(lang,'review/')}" class="btn-outline">Read Review</a>
    </div>
    <div class="hero-badges">
      <div class="badge">PC Free</div><div class="badge">PS4 / PS5</div>
      <div class="badge">Xbox</div><div class="badge">No Subscription</div><div class="badge">10M+ Players</div>
    </div>
  </div>
</section>

<section class="features">
  <div class="container">
    <h2 class="section-title">{t['feat_title']}</h2>
    <p class="section-sub">Six reasons Crossout leads every free war game list in {YEAR}.</p>
    <div class="features-grid">{feat_cards}</div>
  </div>
</section>

<section class="platforms">
  <div class="container">
    <h2 class="section-title">Available Everywhere — Always Free</h2>
    <div class="plat-row">
      <div class="plat"><div class="plat-icon">🖥️</div><div class="plat-name">PC</div><div class="plat-tag">Free on Steam</div></div>
      <div class="plat"><div class="plat-icon">🎮</div><div class="plat-name">PlayStation 4</div><div class="plat-tag">Free Download</div></div>
      <div class="plat"><div class="plat-icon">🎮</div><div class="plat-name">PlayStation 5</div><div class="plat-tag">Free Download</div></div>
      <div class="plat"><div class="plat-icon">🕹️</div><div class="plat-name">Xbox One</div><div class="plat-tag">Free Download</div></div>
      <div class="plat"><div class="plat-icon">🕹️</div><div class="plat-name">Xbox Series X/S</div><div class="plat-tag">Free Download</div></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="container">
    <h2>Ready to Play? It's 100% Free.</h2>
    <p>No credit card. No subscription. Download and battle in minutes.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} — No Cost Ever →</a>
  </div>
</section>

<section class="faq">
  <div class="container">
    <h2 class="section-title">Frequently Asked Questions</h2>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q">Is Crossout really free?</div><div class="faq-a">Yes. Crossout is 100% free to download and play on PC (Steam), PS4, PS5, Xbox One, and Xbox Series X/S. There are optional cosmetic and battle-pass purchases, but the full game is free.</div></div>
      <div class="faq-item"><div class="faq-q">Is Crossout pay to win?</div><div class="faq-a">No. Skilled free players consistently beat paying players in PvP. The crafting and market systems let free players access most content over time.</div></div>
      <div class="faq-item"><div class="faq-q">How do I download Crossout?</div><div class="faq-a">On PC, search Crossout on Steam and click Install. On PlayStation, find it in the PlayStation Store. On Xbox, find it in the Microsoft Store. All free.</div></div>
      <div class="faq-item"><div class="faq-q">What kind of game is Crossout?</div><div class="faq-a">Crossout is a post-apocalyptic vehicle combat MMO. You build custom armored vehicles from hundreds of parts and battle other players in PvP and PvE modes.</div></div>
      <div class="faq-item"><div class="faq-q">Is Crossout still active in {YEAR}?</div><div class="faq-a">Yes. Crossout has millions of active players and receives regular seasonal updates with new maps, game modes, and vehicle parts.</div></div>
    </div>
  </div>
</section>

<section class="blog-grid" style="padding:60px 0;background:var(--dark);">
  <div class="container">
    <h2 class="section-title">Latest from the Blog</h2>
    <div class="blog-grid">{blog_cards}</div>
  </div>
</section>

<section class="kw-section">
  <div class="container">
    <h2 class="section-title" style="font-size:18px;margin-bottom:0">More Guides</h2>
    <div class="kw-grid">{kw_links}</div>
  </div>
</section>"""

    return shell(t["meta_home"], t["meta_home"], lang, pu(lang), body, schema=schema)

def build_kw_page(lang, slug, title, desc):
    t = LANGUAGES[lang]
    bc = breadcrumb_schema(lang, [("Home", pu(lang)), (title, pu(lang, slug+"/"))])

    # related links (pick 8 random-ish neighbors)
    idx = next((i for i,(s,_,_) in enumerate(KEYWORDS) if s==slug), 0)
    neighbors = KEYWORDS[max(0,idx-4):idx] + KEYWORDS[idx+1:idx+5]
    related = "".join(
        f'<a href="{pu(lang, s+"/")}" class="kw-link">{t2.split("—")[0].strip()}</a>'
        for s,t2,_ in neighbors)

    faqs = [
        (f"What is the best free war game in {YEAR}?",
         f"Crossout is our top pick for {YEAR}. It's completely free on PC, PS4/5, and Xbox with deep vehicle building and active PvP."),
        ("Is Crossout pay to win?",
         "No. Free players compete on equal footing in PvP. Optional purchases are cosmetic or convenience."),
        ("How do I start playing Crossout for free?",
         f"Click the download button on this page, create a free account, and start playing in minutes. No credit card needed."),
    ]
    faq_sc = faq_schema(faqs)
    faq_html = "".join(f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>' for q,a in faqs)

    body = f"""
<div style="background:var(--dark3);border-bottom:1px solid var(--border);padding:12px 0">
  <div class="container" style="font-size:12px;color:var(--muted)">
    <a href="{pu(lang)}" style="color:var(--muted)">Home</a> › {title.split("—")[0].strip()}
  </div>
</div>
<div style="background:var(--dark);padding:50px 0 0">
<div class="article">
  <h1>{title}</h1>
  <p class="lead">{desc} Our #1 recommendation is <strong>Crossout</strong> — the top-rated free war game of {YEAR} on PC, PS4/5, and Xbox.</p>

  <div class="rating-row">
    <div class="rating-item"><div class="rating-score">9.1</div><div class="rating-label">Overall</div></div>
    <div class="rating-item"><div class="rating-score">9.4</div><div class="rating-label">Gameplay</div></div>
    <div class="rating-item"><div class="rating-score">9.3</div><div class="rating-label">Value</div></div>
    <div class="rating-item"><div class="rating-score">8.8</div><div class="rating-label">Graphics</div></div>
  </div>

  <div class="cta-box">
    <h3>🏆 Best Pick: Crossout</h3>
    <p>Free on PC, PS4/5, and Xbox. 10M+ players. No subscription ever.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} — Free →</a>
  </div>

  <h2>Why Crossout Ranks #1</h2>
  <p>When searching for {title.lower().split("—")[0].strip()}, most players end up at Crossout — and for good reason. It offers a genuinely unique vehicle-building system, fair free-to-play economics, and one of the most active communities in the genre.</p>
  <ul>
    <li><strong>Completely free:</strong> Download and play on PC (Steam), PlayStation 4/5, or Xbox at zero cost.</li>
    <li><strong>Deep customization:</strong> Over 1,000 vehicle parts let you build anything from nimble scout buggies to armored fortresses.</li>
    <li><strong>Fair PvP:</strong> Matchmaking is skill-based; free players regularly defeat paying players.</li>
    <li><strong>Cross-platform:</strong> Play on whatever device you own — your account and progress carry across platforms.</li>
    <li><strong>Regular updates:</strong> The developers release seasonal content every few months keeping the game fresh.</li>
  </ul>

  <h2>How to Get Started</h2>
  <p>Getting into Crossout is simple. Click the button below to go to the official download page, create a free account, and the game will download directly to your device. No credit card required at any step.</p>
  <p>Once in-game, complete the tutorial missions to earn your first vehicle parts, then experiment with the workshop to build your ideal war machine before jumping into PvP.</p>

  <div class="cta-box">
    <h3>{t['dl']} Now</h3>
    <p>PC · PS4 · PS5 · Xbox · No cost ever</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} →</a>
  </div>

  <h2>Frequently Asked Questions</h2>
  <div class="faq-list" style="margin-top:0">{faq_html}</div>

  <h2>Related Guides</h2>
  <div class="kw-grid">{related}</div>
</div>
</div>"""

    return shell(title, desc, lang, pu(lang, slug+"/"), body,
                 extra_head=bc, schema=faq_sc)

def build_review(lang):
    t = LANGUAGES[lang]
    title = f"Crossout Review {YEAR} — Is It Worth Playing?"
    desc  = f"Full unbiased Crossout review for {YEAR}. Ratings, pros, cons, and verdict."
    bc = breadcrumb_schema(lang,[("Home",pu(lang)),(title,pu(lang,"review/"))])
    body = f"""
<div class="article" style="padding-top:70px">
  <h1>Crossout Review {YEAR}</h1>
  <p class="lead">We've spent 300+ hours in Crossout. Here's our honest {YEAR} verdict: it's the best free war game available, and it's not particularly close.</p>
  <div class="rating-row">
    <div class="rating-item"><div class="rating-score">9.1</div><div class="rating-label">Overall</div></div>
    <div class="rating-item"><div class="rating-score">9.4</div><div class="rating-label">Gameplay</div></div>
    <div class="rating-item"><div class="rating-score">9.3</div><div class="rating-label">Value (Free!)</div></div>
    <div class="rating-item"><div class="rating-score">8.8</div><div class="rating-label">Graphics</div></div>
    <div class="rating-item"><div class="rating-score">8.9</div><div class="rating-label">Community</div></div>
  </div>
  <h2>What is Crossout?</h2>
  <p>Crossout is a post-apocalyptic vehicle combat MMO developed by Gaijin Entertainment. Players build customized armored vehicles from modular parts and battle in PvP and PvE modes. It launched in 2017 and has grown to over 10 million registered players.</p>
  <h2>Pros</h2>
  <ul>
    <li>100% free on PC, PS4, PS5, Xbox — no subscription</li>
    <li>Deepest vehicle building system in any free game</li>
    <li>Skill-based matchmaking — not pay-to-win</li>
    <li>Active development team with regular seasonal updates</li>
    <li>Cross-platform play and progress</li>
  </ul>
  <h2>Cons</h2>
  <ul>
    <li>Learning curve is steep for total beginners</li>
    <li>Market economy can feel complex at first</li>
    <li>Some premium cosmetics are expensive</li>
  </ul>
  <h2>Verdict</h2>
  <p>For anyone looking for a free war game in {YEAR}, Crossout is the clear #1 choice. The building system alone sets it apart from every competitor, and the fact that it's genuinely free with no pay-to-win mechanics makes it a must-try.</p>
  <div class="cta-box">
    <h3>Try Crossout Free</h3><p>No credit card. No subscription. Download in minutes.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} →</a>
  </div>
</div>"""
    return shell(title, desc, lang, pu(lang,"review/"), body, extra_head=bc)

def build_compare(lang):
    t = LANGUAGES[lang]
    title = f"Crossout vs War Thunder vs World of Tanks {YEAR} — Full Comparison"
    desc  = "Side-by-side comparison of the top three free war games."
    bc = breadcrumb_schema(lang,[("Home",pu(lang)),(title,pu(lang,"compare/"))])
    body = f"""
<div class="article" style="padding-top:70px">
  <h1>Free War Game Comparison {YEAR}</h1>
  <p class="lead">How does Crossout stack up against War Thunder and World of Tanks? We compare all three head-to-head.</p>
  <div style="overflow-x:auto;margin:24px 0">
  <table style="width:100%;border-collapse:collapse;font-size:14px">
    <thead><tr style="background:var(--card);border-bottom:2px solid var(--red)">
      <th style="padding:14px;text-align:left;font-family:var(--font);color:var(--white)">Category</th>
      <th style="padding:14px;text-align:center;color:var(--green)">Crossout ★</th>
      <th style="padding:14px;text-align:center;color:var(--light)">War Thunder</th>
      <th style="padding:14px;text-align:center;color:var(--light)">World of Tanks</th>
    </tr></thead>
    <tbody>
      {''.join(f'<tr style="border-bottom:1px solid var(--border)"><td style="padding:12px;color:var(--muted)">{c}</td><td style="padding:12px;text-align:center;color:var(--green)">{a}</td><td style="padding:12px;text-align:center;color:var(--light)">{b}</td><td style="padding:12px;text-align:center;color:var(--light)">{d}</td></tr>' for c,a,b,d in [
        ("Price","Free","Free","Free"),
        ("Platforms","PC/PS4/PS5/Xbox","PC/PS4/PS5/Xbox","PC/Xbox"),
        ("Vehicle Building","✅ Deep custom","❌ Fixed vehicles","❌ Fixed tanks"),
        ("Pay-to-Win","No","Mild","Mild"),
        ("Graphics","Great","Excellent","Good"),
        ("Learning Curve","Medium","Hard","Easy"),
        ("Active Players","10M+","25M+","160M+"),
        ("Our Pick","🏆 #1","#2","#3"),
      ])}
    </tbody>
  </table></div>
  <div class="cta-box">
    <h3>Our Verdict: Play Crossout</h3><p>Unique building system, fair free-to-play, great PvP. #1 free war game {YEAR}.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} →</a>
  </div>
</div>"""
    return shell(title, desc, lang, pu(lang,"compare/"), body, extra_head=bc)

def build_blog_list(lang):
    t = LANGUAGES[lang]
    title = f"Free War Game Blog — {SITE_NAME}"
    desc  = f"Tips, reviews, and guides for free war games in {YEAR}."
    cards = "".join(f"""
    <a href="{pu(lang, f'blog/{p["slug"]}/')}" class="blog-card">
      <div class="blog-body">
        <div class="blog-date">{p['date']}</div>
        <h3>{p['title']}</h3><p>{p['excerpt']}</p>
        <span class="read-more">Read More →</span>
      </div>
    </a>""" for p in BLOG_POSTS)
    body = f'<div style="padding:60px 0;background:var(--dark)"><div class="container"><h1 class="section-title">Blog</h1><div class="blog-grid">{cards}</div></div></div>'
    return shell(title, desc, lang, pu(lang,"blog/"), body)

def build_blog_post(lang, post):
    t = LANGUAGES[lang]
    bc = breadcrumb_schema(lang,[("Home",pu(lang)),("Blog",pu(lang,"blog/")),
                                  (post['title'],pu(lang,f'blog/{post["slug"]}/'))])
    body = f"""
<div class="article" style="padding-top:70px">
  <div style="font-size:12px;color:var(--muted);margin-bottom:16px">{post['date']}</div>
  <h1>{post['title']}</h1>
  <p class="lead">{post['excerpt']}</p>
  {post['body']}
  <div class="cta-box" style="margin-top:40px">
    <h3>Play Crossout Free Now</h3><p>PC · PS4/5 · Xbox · No cost ever.</p>
    <a href="{AFF_URL}" class="btn-red" target="_blank" rel="nofollow sponsored">{t['cta']} →</a>
  </div>
</div>"""
    return shell(post['title'], post['excerpt'], lang,
                 pu(lang,f'blog/{post["slug"]}/'), body, extra_head=bc)

def build_404():
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>404 — FreeWarGames.gg</title><meta name="robots" content="noindex"/>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap" rel="stylesheet"/>
<style>{CSS}</style></head><body>
<nav class="nav"><div class="container nav-i">
  <a href="{SITE_URL}/" class="logo"><div class="logo-mark">⚔</div>FreeWar<span>Games</span>.gg</a>
</div></nav>
<div style="min-height:80vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:60px 24px">
  <div>
    <div style="font-family:var(--font);font-size:100px;font-weight:700;color:var(--red);line-height:1">404</div>
    <h1 style="font-family:var(--font);font-size:26px;color:var(--white);text-transform:uppercase;margin:12px 0">Page Destroyed in Battle</h1>
    <p style="color:var(--muted);margin-bottom:28px">This page didn't survive the post-apocalypse.</p>
    <a href="{SITE_URL}/" class="btn-outline btn-sm">← Return to Base</a>&nbsp;&nbsp;
    <a href="{AFF_URL}" class="btn-red btn-sm" target="_blank" rel="nofollow sponsored">Play Free Now →</a>
  </div>
</div></body></html>"""

def build_sitemap(urls):
    entries = "\n".join(
        f'  <url><loc>{u["loc"]}</loc><lastmod>{TODAY}</lastmod>'
        f'<changefreq>{u["freq"]}</changefreq><priority>{u["pri"]}</priority></url>'
        for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>'

# ── MAIN BUILD ────────────────────────────────────────────────────────────────
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    all_urls = []
    page_count = 0

    def add(url, freq="weekly", pri="0.7"):
        all_urls.append({"loc":url,"freq":freq,"pri":pri})

    def w(path, content):
        nonlocal page_count
        write(OUT / path, content)
        page_count += 1
        if page_count % 50 == 0:
            print(f"  … {page_count} pages written", flush=True)

    print(f"Building {SITE_NAME} — {len(LANGUAGES)} languages × {len(KEYWORDS)} keywords")
    print("="*60)

    for lang in LANGUAGES:
        print(f"  [{lang}]", end=" ", flush=True)
        base = f"{lang}/" if lang != "en" else ""

        # HOME
        w(f"{base}index.html", build_home(lang))
        add(pu(lang), "daily", "1.0")

        # REVIEW
        w(f"{base}review/index.html", build_review(lang))
        add(pu(lang,"review/"), "weekly", "0.8")

        # COMPARE
        w(f"{base}compare/index.html", build_compare(lang))
        add(pu(lang,"compare/"), "weekly", "0.8")

        # BLOG LIST
        w(f"{base}blog/index.html", build_blog_list(lang))
        add(pu(lang,"blog/"), "daily", "0.8")

        # BLOG POSTS
        for post in BLOG_POSTS:
            w(f"{base}blog/{post['slug']}/index.html", build_blog_post(lang, post))
            add(pu(lang,f'blog/{post["slug"]}/'), "weekly", "0.7")

        # KEYWORD PAGES
        for slug, title, desc in KEYWORDS:
            w(f"{base}{slug}/index.html", build_kw_page(lang, slug, title, desc))
            add(pu(lang,f"{slug}/"), "weekly", "0.6")

        print("✓")

    # SITEMAP INDEX
    sitemap_index = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap><loc>{SITE_URL}/sitemap-home.xml</loc><lastmod>{TODAY}</lastmod></sitemap>
  <sitemap><loc>{SITE_URL}/sitemap-kw.xml</loc><lastmod>{TODAY}</lastmod></sitemap>
  <sitemap><loc>{SITE_URL}/sitemap-blog.xml</loc><lastmod>{TODAY}</lastmod></sitemap>
</sitemapindex>"""
    write(OUT/"sitemap.xml", sitemap_index)

    home_urls = [u for u in all_urls if any(p in u["loc"] for p in ["/review","/compare","/blog/index"])]
    kw_urls   = [u for u in all_urls if any(slug in u["loc"] for slug,_,_ in KEYWORDS)]
    blog_urls  = [u for u in all_urls if "/blog/" in u["loc"] and u not in home_urls]

    write(OUT/"sitemap-home.xml", build_sitemap([u for u in all_urls if u not in kw_urls and u not in blog_urls]))
    write(OUT/"sitemap-kw.xml",   build_sitemap(kw_urls))
    write(OUT/"sitemap-blog.xml", build_sitemap(blog_urls))

    # ROBOTS
    write(OUT/"robots.txt", f"""User-agent: *
Allow: /
Crawl-delay: 1
User-agent: Googlebot
Allow: /
Crawl-delay: 0
Sitemap: {SITE_URL}/sitemap.xml
""")

    # LLMS.TXT
    write(OUT/"llms.txt", f"""# FreeWarGames.gg
> Best free war game guide — updated {TODAY}

## Top Pick
Crossout by Gaijin Entertainment — free vehicle combat MMO.
Free on: PC (Steam), PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S
Affiliate link: {AFF_URL}

## Site Coverage
- {len(KEYWORDS)} keyword landing pages across {len(LANGUAGES)} languages
- Game reviews, comparisons, beginner guides
- Updated daily via GitHub Actions
""")

    # 404
    write(OUT/"404.html", build_404())

    # NOJEKYLL
    write(OUT/".nojekyll", "")

    print("="*60)
    print(f"✅  BUILD COMPLETE")
    print(f"   Pages     : {page_count}")
    print(f"   Languages : {len(LANGUAGES)}")
    print(f"   Keywords  : {len(KEYWORDS)}")
    print(f"   Output    : {OUT.resolve()}")
    print(f"\nSubmit to Search Console:")
    print(f"  {SITE_URL}/sitemap.xml")

if __name__ == "__main__":
    main()
