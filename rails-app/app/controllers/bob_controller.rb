class BobController < ApplicationController
  def index
    render json: Wooooss.all.to_json
  end
end
