from os import getenv
from config_market import MARKET
#cache server
EQ_USE_CACHE = False
EQ_CACHE_SERVER = 'http://localhost:9300'
#log and paths
REPO_HOME = "%s/eego" % getenv('HOME')
SYS_HOME = "%s/src" % (REPO_HOME)
DATASTORE_HOME="%s/datastore" % (REPO_HOME)
DATASTORE_EQ_HOME="%s/eq" % (DATASTORE_HOME)
SD_DATA_DIR= "%s/%s/sd_data" % (DATASTORE_EQ_HOME, MARKET)
TD_TRADE_DIR= "%s/user/zy/td_trade" % (DATASTORE_HOME)
RD_REPORT_DIR= "%s/user/zy/rd_report" % (DATASTORE_HOME)
TD_DIVIDEND_DIR= "%s/%s/td_dividend" % (DATASTORE_EQ_HOME, MARKET)
RP_TECHNA_DIR= "%s/%s/rp_techna" % (DATASTORE_EQ_HOME, MARKET)
RP_STRATEGY_DIR= "%s/%s/rp_strategy" % (DATASTORE_EQ_HOME, MARKET)

# logger
EQ_LOG_FILE    = "%s/log/jzlogger.conf" % (SYS_HOME)
EQ_LOGGER_NAME = "main"

BUSINESS_DATES_OF_YEAR = 250

#realtime
YAHOO_MK_LABELS = ['Symbol','LastTradePriceOnly','Open','DayLow', 'DayHigh','PreviousClose','Volume','AverageDailyVolume3Month',\
                    'BookValue','MarketCapitalization','PercentChangeFrom52_weekLow','PercebtChangeFrom52_weekHigh',\
                    'Price_Book','Price_Sales','ChangeinPercent',]
YAHOO_STATIC_DATA_LABELS = ['Symbol','Name','MarketCapitalization','P_ERatio','PEGRatio','P_ERatioRT']
BASEURL = "http://download.finance.yahoo.com/d/quotes.csv?s=${SYMBOLS}&f=${TAGS}&e=.csv"

YAHOO_TAG_FILE = "%s/yahoo_tags.dat" % (SD_DATA_DIR)
STATIC_MARKET_DATA_FILE = "%s/static_data.csv" % (SD_DATA_DIR)

SHORT_LIST = "%s/short_list.csv" % (TD_TRADE_DIR)
WATCH_SYMBOLS_FILE = "%s/watch_symbols.txt" % (TD_TRADE_DIR)
SHORT_LIST_SYMBOLS_FILE = "%s/short_list_symbols.txt" % (TD_TRADE_DIR)
BLOCK_LIST_SYMBOLS_FILE = "%s/block_list.txt" %(TD_TRADE_DIR)
LIVE_SOURCE = "%s/live.csv"% (TD_TRADE_DIR)
DEAD_SOURCE = "%s/dead.csv"% (TD_TRADE_DIR)
DEAD_SOURCE2 = "%s/dead2.csv"% (TD_TRADE_DIR)
MACRO_MARKET_SOURCE = "%s/macro_market.csv"% (TD_TRADE_DIR)
WATCH_SOURCE = "%s/watch.csv" % (TD_TRADE_DIR)

PL_LIVE_REPORT_FILE = "%s/rd_live.csv" % (RD_REPORT_DIR)
PL_DEAD_REPORT_FILE = "%s/rd_dead.csv" %(RD_REPORT_DIR)
PL_STAT_REPORT_FILE = "%s/rd_stat.csv" %(RD_REPORT_DIR)
PL_REPORT_EXPOSURE_FILE = "%s/rd_exposure.csv" % (RD_REPORT_DIR)
MACRO_MARKET_REPORT_FILE = "%s/rd_macro_market.csv" % (RD_REPORT_DIR)

REALTIME_MARKET_DATA_DIR = "%s/%s/md_realtime" % (DATASTORE_EQ_HOME, MARKET)
SD_DATA_DIR = "%s/%s/sd_data" % (DATASTORE_EQ_HOME, MARKET)
EOD_MARKET_DATA_DIR = "%s/%s/md_history" % (DATASTORE_EQ_HOME, MARKET)
RP_TECHNA_DIR = "%s/%s/rp_techna" % (DATASTORE_EQ_HOME, MARKET)




#history

EOD_MKDATA_BASEURL = "http://ichart.finance.yahoo.com/table.csv"
EOD_MKDATA_HIST_DAILY = "%s?s={SYMBOL}&g=d" % (EOD_MKDATA_BASEURL)
EOD_MKDATA_HIST_DIV = "%s?s={SYMBOL}&g=v" % (EOD_MKDATA_BASEURL)
ALL_STOCK_FILE = "%s/all_symbols.txt" % (SD_DATA_DIR)
COMPOSITE_INDEX_SYMBOLS_FILE = "%s/composite_index_symbols.txt" % (SD_DATA_DIR)
OBSOLETE_STOCK_FILE = "%s/obsolete_list.txt" % (SD_DATA_DIR)

MA_FILE_HEADER = ['Date', 'MA_DailyAvg','MA_AdjClose']
MA_FIGURE_ALL_DIR = '%s/%s/ma_fig/all' % (DATASTORE_EQ_HOME,MARKET)
MA_FIGURE_WATCH_DIR = '%s/%s/ma_fig/watch' % (DATASTORE_EQ_HOME,MARKET)
MA_FIGURE_LIVE_DIR = '%s/%s/ma_fig/live' % (DATASTORE_EQ_HOME,MARKET)
MA_FIGURE_SHORT_LIST_DIR = '%s/%s/ma_fig/short_list' % (DATASTORE_EQ_HOME,MARKET)
MA_FIGURE_BLOCK_LIST_DIR = '%s/%s/ma_fig/block_list' % (DATASTORE_EQ_HOME,MARKET)
MA_FIGURE_STI_LIST_DIR = '%s/%s/ma_fig/composite_index_list' % (DATASTORE_EQ_HOME,MARKET)

# History data statistics
STAT_NUM_OF_YEAR_COVERED = 2
STAT_STOCK_TAG = 'stock'
STAT_DATE_TAG = 'dates'
STAT_CLOSE_TAG = 'close'
STAT_MA_TAG = 'ma'
STAT_ADJ_MA_TAG = 'adj_ma'
STAT_AVG_PRICE_TAG = 'avg_price'
STAT_AVG_VOLUME_TAG = 'avg_volume'

#selector
MIN_PRICE_MEAN = 0.2
MAX_PRICE_MEAN = 20
MIN_TRADED_SIZE_MEAN = 2000000 #2M
MIN_TRADED_SIZE_PERC = 0.1 # 0.1%
MIN_MARKET_CAP = 500000000 #0.5B
DAYS_BACKWARD = [7, 14, 30, 90, 180, 365]
#DAYS_BACKWARD = [14]

# Pricing
SGX_TRANSACTION_COST_PERC = 0.002325

#dividend
DIV_HTML_DIR='%s/html' % (TD_DIVIDEND_DIR)
DIV_CSV_DIR='%s/csv' % (TD_DIVIDEND_DIR)
DIV_REPORT_DIR='%s/csv' % (TD_DIVIDEND_DIR)

DIV_TWO_DAYS_REPORT = '%s/div_two_days.csv' % (DIV_REPORT_DIR)
DIV_TWO_MONTHS_REPORT = '%s/div_two_months.csv' % (DIV_REPORT_DIR)
DIV_REPORT_SINCE_LAST_YEAR = '%s/div_since_last_year.csv' % (DIV_REPORT_DIR)
DIV_REPORT_LIVE = '%s/div_live.csv' % (DIV_REPORT_DIR)
DIV_REPORT_WATCH = '%s/div_watch.csv' % (DIV_REPORT_DIR) 
DIV_REPORT_SHORTLIST = '%s/div_shortlist.csv'  % (DIV_REPORT_DIR)
DIV_REPORT_STI = '%s/div_sti.csv'  % (DIV_REPORT_DIR)

#Watch filtering
WATCH_FILT_MIN_SPOT = 0.5
WATCH_FILT_MIN_DAY_CHANGE = 0.6 
WATCH_FILT_MIN_VOL_K = 1000
WATCH_FILT_MAX_DAILY_SL_NUM = 10
WATCH_FILT_MAX_WEEKLY_SL_NUM = 50

# cache 
CACHE_HEADER_TAG = 'HEADER'

# market moving
STOCK_MOVING_FILE =  '%s/mover_all.csv' % (RP_TECHNA_DIR)
STOCK_MOVING_STI_FILE =  '%s/mover_bc.csv' % (RP_TECHNA_DIR)
STOCK_MOVING_SHORTLIST_FILE =  '%s/mover_shortlist.csv' % (RP_TECHNA_DIR)
STOCK_MOVING_WATCH_FILE =  '%s/mover_watch.csv' % (RP_TECHNA_DIR)

# Return
RETURN_COL_DATE = 'Date'
RETURN_COL_DAILY_RETURN = 'DailyReturn'
RETURN_COL_WEEKLY_RETURN = 'WeeklyReturn'
RETURN_COL_MONTHLY_RETURN = 'MonthlyReturn'
RETURN_FILE_HEADER = [RETURN_COL_DATE, RETURN_COL_DAILY_RETURN,RETURN_COL_WEEKLY_RETURN,RETURN_COL_MONTHLY_RETURN]
DAILY_RETURN_STD_TAG = '%sStd' % RETURN_COL_DAILY_RETURN
WEEKLY_RETURN_STD_TAG = '%sStd' % RETURN_COL_WEEKLY_RETURN
MONTHLY_RETURN_STD_TAG = '%sStd'  %  RETURN_COL_MONTHLY_RETURN

DAILY_BAD_OUTLINER_TAG = '%sBadOutliner' % RETURN_COL_DAILY_RETURN
WEEKLY_BAD_OUTLINER_TAG = '%sBadOutliner' % RETURN_COL_WEEKLY_RETURN
MONTHLY_BAD_OUTLINER_TAG = '%sBadOutliner'  %  RETURN_COL_MONTHLY_RETURN
DAILY_GOOD_OUTLINER_TAG = '%sGoodOutliner' % RETURN_COL_DAILY_RETURN
WEEKLY_GOOD_OUTLINER_TAG = '%sGoodOutliner' % RETURN_COL_WEEKLY_RETURN
MONTHLY_GOOD_OUTLINER_TAG = '%sGoodOutliner'  %  RETURN_COL_MONTHLY_RETURN

DAILY_STOP_LOSS_LEVEL1 = -2
DAILY_STOP_LOSS_LEVEL2 = -5 
WEEKLY_STOP_LOSS_LEVEL1 = -2
WEEKLY_STOP_LOSS_LEVEL2 = -5 
MONTHLY_STOP_LOSS_LEVEL1 = -2
MONTHLY_STOP_LOSS_LEVEL2 = -5 

DAILY_STOP_LOSS_LEVEL1_TAG =  '%sSTOPLOSS2' % RETURN_COL_DAILY_RETURN
DAILY_STOP_LOSS_LEVEL2_TAG =  '%sSTOPLOSS5' % RETURN_COL_DAILY_RETURN
WEEKLY_STOP_LOSS_LEVEL1_TAG = '%sSTOPLOSS2' % RETURN_COL_WEEKLY_RETURN
WEEKLY_STOP_LOSS_LEVEL2_TAG = '%sSTOPLOSS5' % RETURN_COL_WEEKLY_RETURN
MONTHLY_STOP_LOSS_LEVEL1_TAG = '%sSTOPLOSS2' % RETURN_COL_MONTHLY_RETURN
MONTHLY_STOP_LOSS_LEVEL2_TAG = '%sSTOPLOSS5' % RETURN_COL_MONTHLY_RETURN

# return reporting
STOCK_RETURN_FILE =  '%s/return_all.csv' % (RP_TECHNA_DIR)
STOCK_RETURN_BLOCK_FILE =  '%s/return_block.csv' % (RP_TECHNA_DIR)
STOCK_RETURN_STI_FILE =  '%s/return_bc.csv' % (RP_TECHNA_DIR)
STOCK_RETURN_SHORTLIST_FILE =  '%s/return_shortlist.csv' % (RP_TECHNA_DIR)
STOCK_RETURN_WATCH_FILE =  '%s/return_watch.csv' % (RP_TECHNA_DIR)
STOCK_RETURN_REPORT_FILE_HEADER = ['Stock', 'Name', 'PE', 'Volume(k)', 'Spot','open','low','high','DayChg', 'WekChg', 'MonChg', 'DayRtn', 'Bd','Gd','SL1','SL2','WekRtn', 'Bd', 'Gd', 'SL1','SL2','MthRtn','Bd', 'Gd', 'SL1','SL2','vol2D rng','vol7D rng','1p rng','2p rng','5p rng']

# reference date for major events
MACRO_EVENT_REF_DATE_1 = '2016-01-28'
MACRO_EVENT_REF_DATE_2 = '2016-09-08'

# stragety reporting
