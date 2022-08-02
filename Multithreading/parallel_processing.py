import fire                          # Function-commandoization
import urllib3                       # HTTP communication
import time                          # Mesure time
from joblib import Parallel, delayed # Parallel processing
import matplotlib.pyplot as plt      # Make Graph

# Crawl web page
def crawl_webpage(URL):
    http = urllib3.PoolManager()
    resp = http.request('GET', URL)
    # print(URL, resp.status)

# Crawl webpages by seqnential processing
def crawl_webpages_by_sequential():
    URLs = (
        'http://www.open-std.org/JTC1/SC22/WG14/',         # C
        'https://isocpp.org/',                             # C++
        'https://docs.microsoft.com/ja-jp/dotnet/csharp/', # C#
        'https://www.w3.org/TR/css/',                      # CSS
        'https://html.spec.whatwg.org/multipage/',         # HTML
        'https://go.dev/',                                 # Go
        'https://www.ecma-international.org/',             # Javascript
        'https://www.php.net/',                            # PHP
        'https://www.python.org/',                         # Python
        'https://www.ruby-lang.org/ja/'                    # Ruby
        )

    start_timer = time.time()

    # Iteration for each URL
    for i, URL in enumerate(URLs):
        crawl_webpage(URL)

    stop_timer = time.time()
    print(stop_timer - start_timer)


# Crawl webpages by parallel processing
def crawl_webpages_by_parallel(n_jobs):
    URLs = (
        'http://www.open-std.org/JTC1/SC22/WG14/',         # C
        'https://isocpp.org/',                             # C++
        'https://docs.microsoft.com/ja-jp/dotnet/csharp/', # C#
        'https://www.w3.org/TR/css/',                      # CSS
        'https://html.spec.whatwg.org/multipage/',         # HTML
        'https://go.dev/',                                 # Go
        'https://www.ecma-international.org/',             # Javascript
        'https://www.php.net/',                            # PHP
        'https://www.python.org/',                         # Python
        'https://www.ruby-lang.org/ja/'                    # Ruby
        )

    start_timer = time.time()

    # Parallel processing for each URL
    Parallel(n_jobs=n_jobs)(delayed(crawl_webpage)(URL) for URL in URLs)

    stop_timer = time.time()

    return stop_timer - start_timer


# Create graph of thread and processing time
def create_graph_thread_time():

    time_records = [] # times by parallel processing
    
    # Iteration for each number of iterations
    for n_job in range(1,16):
        time_records.append(crawl_webpages_by_parallel(n_job))
        
    # Create graph of therad and processing time
    plt.plot(range(1, 16), time_records)
    plt.xlabel('number of therads')
    plt.ylabel('timer')
    plt.show()
    
# Function-commandoization
if __name__ == '__main__':
    fire.Fire({'s': crawl_webpages_by_sequential, 
               'p': crawl_webpages_by_parallel, 
               'c': create_graph_thread_time})
