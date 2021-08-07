#include "pch.h"

using namespace winrt;
using namespace Windows::Foundation;
using namespace Windows::Web::Syndication;

int main()
{
    /*
    init_apartment();
    //Uri uri(L"http://aka.ms/cppwinrt");
    //printf("Hello, %ls!\n", uri.AbsoluteUri().c_str());
    hstring newste{ L"I'm trying." };
    std::wcout << newste.c_str() << std::endl;
    printf("A char in newste: %c\n", newste[4]);
    */
    winrt::init_apartment();

    Uri rssFeedUri{ L"https://blogs.windows.com/feed" };
    SyndicationClient syndicationClient;
    SyndicationFeed syndicationFeed = syndicationClient.RetrieveFeedAsync(rssFeedUri).get();
    for (const SyndicationItem syndicationItem : syndicationFeed.Items())
    {
        winrt::hstring titleAsHstring = syndicationItem.Title().Text();
        std::wcout << titleAsHstring.c_str() << std::endl;
    }
}
