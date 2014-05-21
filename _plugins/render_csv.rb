require 'csv'

module RenderCsvFilter
  class Generator < Jekyll::Generator
    safe true
    def generate(site)
      members = CSV.read('community/psc.csv')
      site.data['psc_members'] = members
    end
  end
end
