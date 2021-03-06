# -*- coding: utf-8 -*-


# Scrapy settings for eProcurementScraperCMR project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'eProcurementScraperCMR'

SPIDER_MODULES = ['eProcurementScraperCMR.spiders']
NEWSPIDER_MODULE = 'eProcurementScraperCMR.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))'

CONCURRENT_ITEMS = 10

SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# DOWNLOAD_DELAY = 0.01
