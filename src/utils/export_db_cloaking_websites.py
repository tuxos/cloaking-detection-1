import MySQLdb
import sys, getopt, math
from threading import Thread
from learning_detection_util import write_proto_to_file, read_proto_from_file, valid_instance, average_distance, centroid_distance, read_proto_from_file
from thread_computer import ThreadComputer
import proto.cloaking_detection_pb2 as CD


def output_db(cursor, output_filename):
	observed_sites = CD.ObservedSites()
	for(url, userFilePath) in cursor:
		site = observed_sites.site.add();
		site.name = url;
		site_observation = site.observation.add();
		site_observation.landing_url = url;
		site_observation.file_path = userFilePath;
	write_proto_to_file(observed_sites, output_filename);
		


cnx = MySQLdb.connect(host='localhost',user='root', passwd='asdf', db='LabelDB')
cursor = cnx.cursor()
query_dom = "SELECT url, userFilePath FROM test_intersect_google_dom WHERE label='Yes'";
query_text = "SELECT url, userFilePath FROM test_intersect_google_text WHERE label='Yes'";
cursor.execute(query_dom)
output_db(cursor, 'export_db_cloaking_websites_dom')
cursor.execute(query_text)
output_db(cursor, 'export_db_cloaking_websites_text')


cursor.close();
cnx.close();

