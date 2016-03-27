$LOAD_PATH.unshift(File.dirname(__FILE__)) unless
    $LOAD_PATH.include?(File.dirname(__FILE__)) || $LOAD_PATH.include?(File.expand_path(File.dirname(__FILE__)))
#$LOAD_PATH << '.'

require 'lib/imdb'


class TopTV < Imdb::MovieList
  private
  def document
    @document ||= Nokogiri::HTML(open('http://akas.imdb.com/chart/tvmeter'))
  end
end
# tv.title


def write_file_topTV
  topTVFile = File.new("topTV.csv", "w")
  $topTVs.each do |tv|
    topTVFile.puts tv.title.split(/\n/)[0] + ', ' + tv.id + ', '  + tv.url
  end
  topTVFile.close
end


def write_file_topTVCharacters

  $myjson = {"tv_list" => [] }
  count = 0
  $topTVs.each do |tv|
    title = tv.title.split(/\n/)[0]
    mytv = {:title => title, :id => tv.id, :cast => tv.cast_characters }
    $myjson["tv_list"].push(mytv)
    count += 1
    puts count
  end

  require 'json'
  topTVCharactersFile = File.new("topTVCharacters.json", "w")
  topTVCharactersFile.puts JSON.generate($myjson)
  topTVCharactersFile.close
end


def main
  $topTVs = TopTV.new.movies
  write_file_topTV
  write_file_topTVCharacters
end


if __FILE__ == 0
  main
end