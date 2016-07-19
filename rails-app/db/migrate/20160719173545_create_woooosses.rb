class CreateWoooosses < ActiveRecord::Migration
  def change
    create_table :woooosses do |t|
      t.string "hello"
      t.timestamps null: false
    end
  end
end
